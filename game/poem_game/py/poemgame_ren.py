# This file contains the Ren'Py code for DDLC's poem game.

# The code logic has been rewritten to use the Ren'Py `_ren.py` approach for Python code.

# For the Ren'Py code, see `script-poemgame.rpy` in the `poem_game` directory.

## Not included in the game, but used for IDEs to avoid multiple warnings.
from game.poem_game.py.poemgame_chibi_ren import chibis, chibi_s, chibi_n, chibi_y
from game.poem_game.py.poemwords_ren import poem_word_db, glitch_word, monika_word
import renpy  # type: ignore

poemwinner: dict[int, str] = {
    0: "sayori",
    1: "sayori",
    2: "sayori",
}

poemappeal: dict[str, dict[int, int]] = {
    "sayori": {0: 0, 1: 0, 2: 0},
    "natsuki": {0: 0, 1: 0, 2: 0},
    "yuri": {0: 0, 1: 0, 2: 0},
}

"""renpy
init python:
"""


class PoemGame:
    """
    This class handles the logic for the poem game in DDLC.
    """

    def __init__(self, testing: bool = False):
        """
        Initializes the poem game with default values.

        :param testing: If True, bypasses Ren'Py functions and screens for testing purposes. Unused in DDLC. Used for Github Actions to test code logic.
        :type testing: bool
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

        self.testing = testing

    def reset(self):
        """
        Resets the poem game to its initial state.
        """
        self.played_baa = False
        self.poemgame_glitch = False
        self.poem_progress = 1

    def start(self):
        """
        Starts the poem game.
        This method should be called to initiate the poem game logic.
        """
        self.reset()

        # Resets the points for each character.
        chibis.reset()

        wordList = poem_word_db.get_words()
        if len(wordList) == 0:
            raise ValueError(
                "No words found in the poem word database. Please check `poemwords_ren.py` for poem word declarations."
            )

        while self.poem_progress <= 20:
            random_words: list[str] = []
            for _ in range(10):
                try:
                    word = renpy.random.choice(wordList)
                except IndexError:
                    raise IndexError(
                        "Not enough words in the poem word database. Add more words to `poemwords_ren.py`."
                    )
                random_words.append(word.__str__())
                wordList.remove(
                    word
                )  # Remove the word to avoid duplicates in the same poem game.

            # Display the poem game screen with the random words.
            if self.testing:
                if renpy.persistent.playthrough == 2:
                    act_two_words = random_words[:9]
                    act_two_words.append(glitch_word.word)
                    poemword_str = renpy.random.choice(act_two_words)
                elif renpy.persistent.playthrough == 3:
                    act_three_words = []
                    for _ in range(10):
                        act_three_words.append(monika_word.word)
                    poemword_str = renpy.random.choice(act_three_words)
                else:
                    poemword_str = renpy.random.choice(random_words)
            else:
                poemword_str = renpy.call_screen(
                    "poem_test",
                    words=random_words,
                    progress=self.poem_progress,
                    poemgame_glitch=self.poemgame_glitch,
                )

            # Checks if the word exists in the word database.
            if poemword_str in poem_word_db.get_words_str():
                selected_poemword = poem_word_db.get_word(poemword_str)
            else:
                if renpy.persistent.playthrough == 2:
                    selected_poemword = glitch_word
                else:
                    selected_poemword = monika_word

            if not self.testing:
                if not self.poemgame_glitch:
                    if selected_poemword.glitch_word:
                        self.poemgame_glitch = True
                        renpy.music.play(renpy.audio.t4g)
                        renpy.show("white")
                        # renpy.show("y_sticker_glitch", at_list=[sticker_glitch], zorder=10)
                    elif renpy.persistent.playthrough != 3:
                        renpy.play(renpy.gui.activate_sound)

                        # Act 1
                        if renpy.persistent.playthrough == 0:
                            if selected_poemword.sPoint >= 3:
                                renpy.show("s_sticker hop")
                            elif selected_poemword.nPoint >= 3:
                                renpy.show("n_sticker hop")
                            elif selected_poemword.yPoint >= 3:
                                renpy.show("y_sticker hop")
                        else:
                            # Act 2
                            if (
                                renpy.persistent.playthrough == 2
                                and renpy.store.chapter == 2
                                and renpy.random.randint(0, 10) == 0
                            ):
                                renpy.show(
                                    "m_sticker hop"
                                )  # 1/10 chance to see Monika hopping under the game screen.
                            elif selected_poemword.nPoint > selected_poemword.yPoint:
                                renpy.show(
                                    "n_sticker hop"
                                )  # In Act 2, Natsuki hops if she has more points than Yuri.
                            elif (
                                renpy.persistent.playthrough == 2
                                and not renpy.persistent.seen_sticker
                                and renpy.random.randint(0, 100) == 0
                            ):
                                renpy.show(
                                    "y_sticker hopg"
                                )  # "y_sticker_2g.png". 1/100 chance to see it, if we haven't seen it already.
                                renpy.persistent.seen_sticker = True
                            elif (
                                renpy.persistent.playthrough == 2
                                and renpy.store.chapter == 2
                            ):
                                renpy.show(
                                    "y_sticker_cut hop"
                                )  # Yuri's cut arms sticker
                            else:
                                renpy.show("y_sticker hop")
                else:
                    r = renpy.random.randint(
                        0, 10
                    )  # 1/10 chance to hear a "baa" sound.
                    if r == 0 and not self.played_baa:
                        renpy.play("gui/sfx/baa.ogg")
                        self.played_baa = True
                    elif r <= 5:
                        renpy.play(renpy.gui.activate_sound_glitch)

            chibi_s.add_points(selected_poemword.sPoint)
            chibi_n.add_points(selected_poemword.nPoint)
            chibi_y.add_points(selected_poemword.yPoint)
            self.poem_progress += 1

    def finish(self):
        """
        Finishes the poem game.
        This method should be called to conclude the poem game logic.
        """
        # Act 1 Calculations
        if renpy.persistent.playthrough == 0:
            # Add 5 points to whoever we side with in Act 1 - Chapter 1.
            if renpy.store.chapter == 1:
                chibi = chibis.get_chibi(renpy.store.ch1_choice)
                chibi.add_points(5)

            poemwinner[renpy.store.chapter] = max(
                chibis.chibis, key=lambda c: c.charPointTotal
            ).name
        else:
            # Act 2 Calculations
            if chibi_n.charPointTotal > chibi_y.charPointTotal:
                poemwinner[renpy.store.chapter] = "natsuki"
            else:
                poemwinner[renpy.store.chapter] = "yuri"

        # Add appeal point based on poem winner.
        poemwinner_chibi = chibis.get_chibi(poemwinner[renpy.store.chapter])
        poemwinner_chibi.add_appeal()

        # Set poem appeal
        poemappeal["sayori"][renpy.store.chapter] = chibi_s.calculate_appeal()
        poemappeal["natsuki"][renpy.store.chapter] = chibi_n.calculate_appeal()
        poemappeal["yuri"][renpy.store.chapter] = chibi_y.calculate_appeal()

        # Poem winner alway has appeal of 1.
        poemappeal[poemwinner_chibi.name][renpy.store.chapter] = 1


poem_game = PoemGame()
