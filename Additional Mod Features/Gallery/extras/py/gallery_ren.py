# Авторские права 2019-наст. вр. Азариель Дель Кармен (bronya_rand). Все права защищены.
# Этот файл содержит код Python экрана Галереи.
# Код адаптирован под Ren'Py 8 и использует подход `_ren.py` для кода на Python.

# Чтобы просмотреть код Ren'Py, откройте файл `gallery.rpy` в каталоге `extras`.

## Эти импорты не используются во время запуска игры, но нужны для того, чтобы IDE
## не выдавали кучу предупреждений.
import os
import renpy  # type: ignore
from game.definitions.py.core_ren import persistent

persistent.unlocked_gallery_images = []

"""renpy
init python:
"""


class GalleryBase:
    """
    Класс, представляющий собой базу для изображений в галерее.
    """

    def __init__(
        self,
        img: str,
        small_img: str | None = None,
        export_img_name: str | None = None,
        name: str | None = None,
        artist: str | None = None,
        description: str | None = None,
        bg: str | None = None,
        sprite: bool = False,
        exportable: bool = True,
        unlock_by_default: bool = False,
    ):
        self.name = name if name else img
        self.artist = artist
        self.description = description

        # Открыть доступ, если добавлено в постоянный перечень или должно быть открыто изначально.
        if img in persistent.unlocked_gallery_images or unlock_by_default:
            if unlock_by_default and img not in persistent.unlocked_gallery_images:
                persistent.unlocked_gallery_images.append(img)
            self.unlocked = True
        else:
            self.unlocked = False

        self.sprite = sprite
        self.exportable = exportable

        self.img_file = img
        self.img, self.small_img = self._setup_images(img, small_img, sprite, bg)
        self.bg = (
            renpy.store.Transform(
                bg, size=(renpy.config.screen_width, renpy.config.screen_height)
            )
            if bg
            else None
        )
        self.export_name = export_img_name

    def _setup_images(
        self, img: str, small_img: str | None, sprite: bool, bg: str | None
    ):
        bg = bg if bg else "black"
        if sprite:
            # Спрайт в галерее
            ## С Discord-сервера Ren'Py: Хотя к ним можно обращаться через renpy.display.layout.Composite,
            ## лучше использовать store на случай переопределений/устаревания.
            full_img = renpy.store.Composite(
                (renpy.config.screen_width, renpy.config.screen_height),
                (0, 0),
                bg,
                (0.2 * renpy.config.screen_width / 1280.0, 0),
                renpy.store.Transform(img, zoom=0.75 * 0.95),
            )
            display_img = small_img or renpy.store.Composite(
                (234, 132),
                (0, 0),
                renpy.store.Transform(bg, size=(233, 131), fit="cover"),
                (0.2, 0),
                renpy.store.Transform(img, zoom=0.137),
            )
        else:
            # Фон в галерее
            full_img = renpy.store.Transform(
                img,
                size=(renpy.config.screen_width, renpy.config.screen_height),
                fit="contain",
            )
            display_img = small_img or renpy.store.Composite(
                (234, 132),
                (0, 0),
                renpy.store.Transform(bg, size=(233, 131), fit="cover"),
                (0, 0),
                renpy.store.Transform(img, size=(234, 132)),
            )

        return full_img, display_img

    def unlock(self):
        """
        Открывает изображение для просмотра.
        """
        self.unlocked = True
        persistent.unlocked_gallery_images.append(self.img)

    def lock(self):
        """
        Закрывает изображение, не давая его просматривать.
        """
        self.unlocked = False
        if self.img in persistent.unlocked_gallery_images:
            persistent.unlocked_gallery_images.remove(self.img)

    def get_image(self) -> str:
        """
        Возвращает полный путь к изображению.
        """
        return self.img

    def get_image_name(self) -> str:
        """
        Возвращает название изображения.
        """
        return self.name

    def get_small_image(self) -> str:
        """
        Возвращает путь к маленькому изображению.
        """
        return self.small_img or "mod_assets/mod_extra_images/galleryLock.png"
        # return self.small_img

    def get_image_artist(self) -> str | None:
        """
        Возвращает имя художника.
        """
        return self.artist

    def get_image_description(self) -> str | None:
        """
        Возвращает описание изображения.
        """
        return self.description

    def get_image_background(self):
        """
        Возвращает задний план изображения.
        """
        return self.bg

    def is_exportable(self):
        return self.exportable

    def is_unlocked(self):
        return self.unlocked

    def export_image(self):
        """
        Сохраняет изображение из галереи на физический носитель пользователя.
        """
        if not self.exportable:
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Это изображение нельзя экспортировать."),
                ok_action=renpy.store.Hide(),
            )
            return
        # Предотвращаем экспорт спрайтов.
        if self.sprite:
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Спрайты нельзя экспортировать."),
                ok_action=renpy.store.Hide(),
            )
            return

        # Получаем каталог для экспорта.
        export_dir = None
        if renpy.android:
            android_public_dir = os.environ.get("ANDROID_PUBLIC_DIRECTORY")
            if not android_public_dir:
                renpy.show_screen(
                    "dialog",
                    message=renpy.store._("Невозможно получить доступ к общедоступному каталогу Android для сохранения изображений."),
                    ok_action=renpy.store.Hide(),
                )
                return

            export_dir = os.path.join(android_public_dir, "gallery")
        else:
            export_dir = os.path.join(renpy.config.basedir, "gallery")
        if export_dir is None:
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Невозможно определить каталог для экспорта."),
                ok_action=renpy.store.Hide(),
            )
            return
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        # Получаем путь к файлу изображения.
        try:
            renpy.open_file(self.img_file)
            renpy_img = self.img_file
        except FileNotFoundError:
            img_filename = self.img_file
            if not isinstance(img_filename, tuple):
                img_filename = tuple(img_filename.split())
            renpy_img = renpy.display.image.images.get(img_filename).filename
        if not renpy_img:
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Невозможно найти файл изображения для экспорта."),
                ok_action=renpy.store.Hide(),
            )
            return

        # Определяем имя экспортируемого файла.
        original_ext = os.path.splitext(renpy_img)[1]

        export_filename = None
        if self.export_name:
            if not os.path.splitext(self.export_name)[1]:
                export_filename = f"{self.export_name}{original_ext}"
            else:
                export_filename = self.export_name
        else:
            export_filename = os.path.basename(renpy_img)
        if not export_filename:
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Невозможно определить имя экспортируемого файла."),
                ok_action=renpy.store.Hide(),
            )
            return

        # Экспортируем изображение.
        img_export_file = os.path.join(export_dir, export_filename)
        if os.path.exists(img_export_file):
            renpy.show_screen(
                "dialog",
                message=renpy.store._("Вы уже экспортировали это изображение."),
                ok_action=renpy.store.Hide(),
            )
            return

        with open(img_export_file, "wb") as outfile:
            try:
                outfile.write(renpy.open_file(renpy_img).read())
            except FileNotFoundError:
                try:
                    # Для доступа к RPA? Вроде работает с изображениями, упакованными в images.rpa, в отличие от open_file.
                    outfile.write(
                        renpy.loader.load(renpy_img, directory="images").read()
                    )
                except Exception as e:
                    renpy.show_screen(
                        "dialog",
                        message=renpy.store._("Ошибка экспорта:") + f" {str(e)}", # если удалить f-string, почему-то начинает ругаться на незакрытую скобку...
                        ok_action=renpy.store.Hide(),
                    )
                    return

        renpy.show_screen(
            "dialog",
            message=renpy.store._("Изображение было сохранено в папку «gallery» в рабочей папке игры."),
            ok_action=renpy.store.Hide(),
        )


class GalleryAltImage(GalleryBase):
    """
    Класс, представляющий собой альтернативную версию изображения в галерее.
    """

    def __init__(
        self,
        img: str,
        small_img: str | None = None,
        export_img_name: str | None = None,
        name: str = "",
        artist: str = "",
        description: str = "",
        bg: str | None = None,
        sprite: bool = False,
        exportable: bool = True,
        unlock_by_default: bool = False,
    ):
        super().__init__(
            img,
            small_img,
            export_img_name,
            name,
            artist,
            description,
            bg,
            sprite,
            exportable,
            unlock_by_default,
        )


class GalleryImage(GalleryBase):
    """
    Класс, представляющий собой изображение в галерее с дополнительными атрибутами.
    """

    def __init__(
        self,
        img: str,
        small_img: str | None = None,
        export_img_name: str | None = None,
        name: str = "",
        artist: str = "",
        description: str = "",
        alts: list[GalleryAltImage] | None = None,
        bg: str | None = None,
        sprite: bool = False,
        exportable: bool = True,
        unlock_by_default: bool = False,
    ):
        super().__init__(
            img,
            small_img,
            export_img_name,
            name,
            artist,
            description,
            bg,
            sprite,
            exportable,
            unlock_by_default,
        )

        if type(alts) is list and all(isinstance(alt, GalleryAltImage) for alt in alts):
            self.alts = list(alts)
        else:
            self.alts = []

    def has_alt_images(self) -> bool:
        """
        Проверяет, есть ли у изображения альтернативные версии.
        """
        return len(self.alts) > 0

    def unlock_alt_image(self, img_index: int) -> None:
        """
        Открывает конкретную альтернативную версию для просмотра.
        """
        if 0 <= img_index < len(self.alts):
            self.alts[img_index].unlock()

    def unlock_all_alt_images(self) -> None:
        for alt in self.alts:
            alt.unlock()

    def lock_alt_image(self, img_index: int) -> None:
        """
        Закрывает конкретную альтернативную версию, не давая её просматривать.
        """
        if 0 <= img_index < len(self.alts):
            self.alts[img_index].lock()

    def lock_all_alt_images(self) -> None:
        for alt in self.alts:
            alt.lock()


class GalleryDB:
    """
    Класс для управления базой данных галереи.
    """

    def __init__(self):
        self.images: list[GalleryImage] = []
        self.image_index: int = 0
        self.alt_index: int = 0

    def add_image(self, image: GalleryImage) -> None:
        """
        Добавляет изображение в базу.

        :param image: Объект GalleryImage, который нужно добавить.
        """
        self.images.append(image)

    def set_image_index(self, index: int) -> None:
        """
        Устанавливает индекс изображения.

        :param index: Индекс, который необходимо задать.
        """
        if 0 <= index < len(self.images):
            self.image_index = index
            self.alt_index = 0

    def get_alt_image_index(self) -> int:
        """
        Возвращает текущий индекс альтернативной версии для конкретного изображения.
        """
        return self.alt_index

    def set_alt_image_index(self, index: int) -> None:
        """
        Устанавливает индекс альтернативной версии для конкретного изображения.

        :param index: Индекс, который необходимо задать альтернативной версии.
        """
        try:
            image = self.get_image()
            if 0 <= index < len(image.alts):
                self.alt_index = index
        except IndexError:
            raise IndexError("Неверный индекс изображения; невозможно задать индекс альтернативной версии.")

    def get_image(self) -> GalleryImage:
        """
        Возвращает конкретное изображение в галерее.
        """
        if len(self.images) == 0:
            raise IndexError("Нет изображений в галерее.")
        try:
            return self.images[self.image_index]
        except IndexError:
            raise IndexError("Неверный индекс изображения.")

    def get_alt_image(self) -> GalleryAltImage:
        """
        Возвращает конкретную альтернативную версию конкретного изображения.
        """
        image = self.get_image()
        if len(image.alts) == 0:
            raise IndexError("У этого изображения нет альтернативных версий.")
        try:
            return image.alts[self.alt_index]
        except IndexError:
            raise IndexError("Неверный индекс альтернативной версии.")

    def has_next_image(self) -> bool:
        """
        Проверяет, есть ли следующее изображение после текущего.
        """
        return len(self.images) > 0 and self.image_index < len(self.images) - 1

    def has_prev_image(self) -> bool:
        """
        Проверяет, есть ли предыдущее изображение перед текущим.
        """
        return len(self.images) > 0 and self.image_index > 0

    def has_next_alt_image(self) -> bool:
        try:
            image = self.get_image()
            return len(image.alts) > 0 and self.alt_index < len(image.alts) - 1
        except IndexError:
            return False

    def has_prev_alt_image(self) -> bool:
        try:
            image = self.get_image()
            return len(image.alts) > 0 and self.alt_index > 0
        except IndexError:
            return False

    def _find_next_unlocked(self) -> int | None:
        """
        Ищет следующее открытое изображение относительно текущего индекса.

        :return: Индекс следующего открытого изображения, либо None, если такого изображения нет.
        :rtype: int | None
        """
        if len(self.images) == 0:
            return None

        # Ищем после текущего индекса.
        for i in range(self.image_index + 1, len(self.images)):
            if self.images[i].is_unlocked():
                return i

        # Заворачиваем и ищем с начала.
        for i in range(0, self.image_index + 1):
            if self.images[i].is_unlocked():
                return i

        return None

    def _find_prev_unlocked(self) -> int | None:
        """
        Ищет предыдущее открытое изображение относительно текущего индекса.

        :return: Индекс предыдущего открытого изображения, либо None, если такого изображения нет.
        :rtype: int | None
        """
        if len(self.images) == 0:
            return None

        # Ищем перед текущим индексом.
        for i in range(self.image_index - 1, -1, -1):
            if self.images[i].is_unlocked():
                return i

        # Заворачиваем и ищем с конца.
        for i in range(len(self.images) - 1, self.image_index - 1, -1):
            if self.images[i].is_unlocked():
                return i

        return None

    def _find_next_alt_unlocked(self) -> int | None:
        """
        Ищет следующую открытую альтернативную версию относительно текущего индекса альт. версии.

        :return: Индекс следующей альтернативной версии, либо None, если такого изображения нет.
        :rtype: int | None
        """
        try:
            image = self.get_image()
        except IndexError:
            return None

        if len(image.alts) == 0:
            return None

        # Ищем после текущего индекса альт. версии.
        for i in range(self.alt_index + 1, len(image.alts)):
            if image.alts[i].is_unlocked():
                return i

        # Заворачиваем и ищем с начала.
        for i in range(0, self.alt_index + 1):
            if image.alts[i].is_unlocked():
                return i

        return None

    def _find_prev_alt_unlocked(self) -> int | None:
        """
        Ищет предыдущую открытую альтернативную версию относительно текущего индекса альт. версии.

        :return: Индекс предыдущей альтернативной версии, либо None, если такого изображения нет.
        :rtype: int | None
        """
        try:
            image = self.get_image()
        except IndexError:
            return None

        if len(image.alts) == 0:
            return None

        # Ищем перед текущим индексом альт. версии.
        for i in range(self.alt_index - 1, -1, -1):
            if image.alts[i].is_unlocked():
                return i

        # Заворачиваем и ищем с конца.
        for i in range(len(image.alts) - 1, self.alt_index - 1, -1):
            if image.alts[i].is_unlocked():
                return i

        return None

    def next_image(self) -> None:
        """
        Получает следующее открытое изображение в галерее.
        """
        next_index = self._find_next_unlocked()
        if next_index is not None:
            self.image_index = next_index
            self.alt_index = 0

    def prev_image(self) -> None:
        """
        Получает предыдущее открытое изображение в галерее.
        """
        prev_index = self._find_prev_unlocked()
        if prev_index is not None:
            self.image_index = prev_index
            self.alt_index = 0

    def next_alt_image(self) -> None:
        """
        Получает следующую открытую альтернативную версию изображения.
        """
        next_index = self._find_next_alt_unlocked()
        if next_index is not None:
            self.alt_index = next_index

    def prev_alt_image(self) -> None:
        """
        Получает предыдущую открытую альтернативную версию изображения.
        """
        prev_index = self._find_prev_alt_unlocked()
        if prev_index is not None:
            self.alt_index = prev_index

    def reset_navigation(self) -> None:
        """
        Сбрасывает индексы навигации в начало.
        """
        self.image_index = 0
        self.alt_index = 0

    def get_images(self) -> list[GalleryImage]:
        """
        Возвращает список изображений в галерее.
        """
        return self.images

    def get_image_count(self) -> int:
        """
        Возвращает количество изображений в галерее.
        """
        return len(self.images)


## Инициализирует глобальную базу данных галереи.
gallery_db = GalleryDB()

## Изображения для примера. Замените или дополните их при необходимости.
residential = GalleryImage("bg residential_day", unlock_by_default=True)
s1a = GalleryImage("sayori 1", sprite=True, unlock_by_default=True)
m1a = GalleryImage("monika 1", name=renpy.store._("Моника"), artist="Satchely", sprite=True)

n2a = GalleryAltImage("natsuki 2", sprite=True, unlock_by_default=True)
n3a = GalleryAltImage("natsuki 3", sprite=True)
n1a = GalleryImage("natsuki 1", sprite=True, unlock_by_default=True, alts=[n2a, n3a])

gallery_db.add_image(residential)
gallery_db.add_image(s1a)
gallery_db.add_image(m1a)
gallery_db.add_image(n1a)
