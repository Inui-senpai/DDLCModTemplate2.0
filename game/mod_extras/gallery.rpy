## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

# gallery.rpy
# Данный файл содержит код меню галереи, отображающей фоны и
# спрайты вашей модификации.

init python:
    import math
    import renpy.display.image as imgcore
    from collections import OrderedDict 

    galleryList = None 
    current_img_name = None

    # Этот класс определяет код для создания изображения для меню Галереи.
    # Синтаксис:
    # image - Эта переменная содержит путь к изображению или тег оного
    #         (напр. sayori 1a).
    # small_size - Эта переменная содержит путь к уменьшенной версии
    #              изображения или тег оной.
    # name - Эта переменная содержит читабельное название изображения
    #        в Галерее.
    # artist - Эта переменная содержит читабельное имя автора изображения.
    # sprite - Эта переменная проверяет, является ли объявленное
    #          изображение спрайтом персонажа.
    # watermark - Эта переменная указывает, должен ли экспортер экспортировать
    #             изображение, добавляемое в Галерею, с водяным знаком.
    # unlocked - Эта переменная проверяет, должно ли это изображение добавляться
    #            в Галерею сразу или только после того, как появится в игре.
    # locked - УПРАЗДНЕНА, используйте «unlocked». Эта переменная использовалась
    #          для блокировки отображения изображения в Галерее.
    class GalleryImage:

        def __init__(self, image, small_size=None, name=None, artist=None, sprite=False, watermark=False, unlocked=True, locked=None):
            global galleryList 

            # Название внутриигровой переменной изображения, содержащегося в игре
            self.file = image

            # Читабельное название изображения
            self.name = name if name else image

            # Читабельное имя автора изображения
            self.artist = artist

            # Это условие указывает, является ли данное изображение спрайтом
            self.sprite = sprite

            # Это условие указывает, заблокировано ли изображение
            if unlocked and locked != True:
                self.unlocked = True
            else:
                self.unlocked = renpy.seen_image(image)

            # Это условие указывает, должно ли изображение экспортироваться с водяным знаком
            self.watermark = watermark

            if sprite:

                self.image = Composite(
                    (1280, 720), (0, 0), 
                    "black", (0.2, 0), 
                    Transform(image, zoom=0.75*0.95)
                )

                # Уменьшенная версия главного изображения
                if small_size:
                    self.small_size = small_size 
                else:               
                    self.small_size = Composite(
                        (234, 132), (0, 0), 
                        "black", (0.2, 0), 
                        Transform(image, zoom=0.137)
                    )
            else:
                
                self.image = Transform(image, size=(1280, 680))

                if small_size:
                    self.small_size = small_size 
                else:     
                    self.small_size = Transform(image, size=(234, 132))

            if galleryList is None:
                galleryList = OrderedDict([(self.name, self)])
            else:
                galleryList[self.name] = self

        # Эта функция экспортирует выбранное изображение на устройство игрока.
        def export(self):

            try: os.mkdir(user_dir + "/gallery")
            except: pass

            if self.sprite:
                renpy.show_screen("dialog", message="Спрайты не могут быть экспортированы в папку галереи. Повторите попытку с другим изображением.", ok_action=Hide("dialog"))
            else:
                try: 
                    renpy.file(self.file)
                    export = self.file
                except:
                    export = get_registered_image(self.file).filename

                with open(os.path.join(user_dir, "gallery", os.path.splitext(export)[0].split("/")[-1] + os.path.splitext(export)[-1]).replace("\\", "/"), "wb") as p:
                    if self.watermark:
                        p.write(renpy.file(os.path.splitext(export)[0] + "_watermark" + os.path.splitext(export)[-1]).read())
                    else:
                        p.write(renpy.file(export).read())

                renpy.show_screen("dialog", message="Изображение «" + self.name + "» было экспортировано в папку галереи.", ok_action=Hide("dialog"))

    # Эта функция переходит к следующему/предыдущему изображению в галерее.
    def next_image(back=False):
        global current_img_name

        # Создаёт новый список на основе ключей словаря
        all_keys = list(galleryList.keys())

        # Берёт текущий ключ в качестве индекса
        current_index = all_keys.index(current_img_name)

        # Берёт следующий ключ в качестве индекса
        next_index = current_index - 1 if back else current_index + 1

        try: 
            all_keys[next_index]
            current_img_name = all_keys[next_index]
        except IndexError: current_img_name = all_keys[0]

    # Для совместимости с Ren'Py 6. Эта функция выводит изображение на экран через «renpy.display.image».
    def get_registered_image(name): 

        if not isinstance(name, tuple):
            name = tuple(name.split())

        return imgcore.images.get(name)

    # В этом разделе объявляются изображения, показываемые в галерее. См. 
    # синтаксис класса «GalleryMenu», чтобы добавить своё изображение.
    residential = GalleryImage("bg residential_day")

    s1a = GalleryImage("sayori 1", sprite=True)

    m1a = GalleryImage("monika 1", name="Моника", artist="Satchely", sprite=True)

## Экран галереи ##############################################################
##
## Этот экран используется для создания галереи внутриигровых артов, которые
## игрок может просмотреть в главном меню.
##
## Синтаксис:
## gl.image - Эта переменная содержит путь к изображению или тег оного
##            (напр. sayori 1a).
## gl.small_size - Эта переменная содержит путь к уменьшенной версии
##                 изображения или тег оной.
## gl.name - Эта переменная содержит читабельное название изображения
##           в галерее.
## gl.sprite - Эта переменная проверяет, является ли объявленное
##             изображение спрайтом персонажа.
## gl.locked - Эта переменная указывает, должно ли добавляться это изображение
##             в галерею, если оно ещё не было увидено в игре.

screen gallery():

    tag menu

    use game_menu(_("Галерея")):
        
        fixed:

            vpgrid:
                id "gvp"

                rows math.ceil(len(galleryList) / 3.0)

                if len(galleryList) > 3:
                    cols 3
                else:
                    cols len(galleryList)

                spacing 25
                mousewheel True

                xalign 0.5
                yalign 0.5

                for name, gl in galleryList.items():

                    if gl.unlocked:
                        vbox:
                            imagebutton: 
                                idle gl.small_size
                                action [SetVariable("current_img_name", name), ShowMenu("preview"), With(Dissolve(0.5))]
                            text "[name]": 
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14
                            if gl.artist:
                                text "Художник: [gl.artist]":
                                    xalign 0.5
                                    color "#555"
                                    outlines []
                                    size 14

            vbar value YScrollValue("gvp") xalign 0.99 ysize 560

## Экран галереи ##################################################################
##
## Этот экран показывает выбранное игроком изображение крупным планом.

screen preview():

    tag menu

    hbox: 
        add galleryList[current_img_name].image yoffset 40
    hbox:
        add Solid("#fcf") size(config.screen_width, 40)

    hbox:
        ypos 0.005
        xalign 0.5 
        text current_img_name: 
            color "#000"
            outlines []
            size 24 

    hbox:
        ypos 0.005
        xalign 0.98
        textbutton "Э":
            text_style "navigation_button_text"
            action Function(galleryList[current_img_name].export) 

        textbutton "Х":
            text_style "navigation_button_text"
            action ShowMenu("gallery")

    textbutton "<":
        text_style "navigation_button_text"
        xalign 0.0
        yalign 0.5
        action Function(next_image, True)

    textbutton ">":
        text_style "navigation_button_text"
        xalign 1.0
        yalign 0.5
        action Function(next_image)

    on "replaced" action With(Dissolve(0.5))
