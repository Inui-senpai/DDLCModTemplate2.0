import os
import renpy  # type: ignore

"""renpy
init -2 python:
"""


class GalleryBase:
    """
    A class representing a base for gallery images.
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

        self.unlocked = unlock_by_default
        self.sprite = sprite
        self.exportable = exportable

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
            # Sprite Gallery Image
            ## From Ren'Py Discord: While you can access this via renpy.display.layout.Composite,
            ## better to use store in case of overrides/deprecations.
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
            # Background Gallery Image
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
        Unlocks the gallery image for viewing.
        """
        self.unlocked = True

    def lock(self):
        """
        Locks the gallery image, preventing viewing.
        """
        self.unlocked = False

    def get_image(self) -> str:
        """
        Returns the full image path.
        """
        return self.img

    def get_image_name(self) -> str:
        """
        Returns the name of the image.
        """
        return self.name

    def get_small_image(self) -> str:
        """
        Returns the small image path.
        """
        return self.small_img or "mod_assets/mod_extra_images/galleryLock.png"
        # return self.small_img

    def get_image_artist(self) -> str | None:
        """
        Returns the artist of the image.
        """
        return self.artist

    def get_image_description(self) -> str | None:
        """
        Returns the description of the image.
        """
        return self.description

    def get_image_background(self):
        """
        Returns the background of the image.
        """
        return self.bg

    def is_exportable(self):
        return self.exportable

    def is_unlocked(self):
        return self.unlocked

    def export_image(self):
        """
        Exports the gallery image to the user's file system.
        """
        if not self.exportable:
            renpy.show_screen(
                "dialog",
                message="This image is not exportable.",
                ok_action=renpy.store.Hide(),
            )
            return
        # Block sprite images from being exported.
        if self.sprite:
            renpy.show_screen(
                "dialog",
                message="Sprite images are not exportable.",
                ok_action=renpy.store.Hide(),
            )
            return

        # Get gallery export directory.
        export_dir = None
        if renpy.android:
            android_public_dir = os.environ.get("ANDROID_PUBLIC_DIRECTORY")
            if not android_public_dir:
                renpy.show_screen(
                    "dialog",
                    message="Unable to access Android public directory for exporting images.",
                    ok_action=renpy.store.Hide(),
                )
                return

            export_dir = os.path.join(android_public_dir, "gallery")
        else:
            export_dir = os.path.join(renpy.config.basedir, "gallery")
        if export_dir is None:
            renpy.show_screen(
                "dialog",
                message="Unable to determine export directory.",
                ok_action=renpy.store.Hide(),
            )
            return
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        # Get the image file path.
        try:
            renpy.open_file(self.img)
            renpy_img = self.img
        except IOError:
            renpy_img = renpy.display.image.images.get(self.img).filename
        if not renpy_img:
            renpy.show_screen(
                "dialog",
                message="Unable to locate image file for export.",
                ok_action=renpy.store.Hide(),
            )
            return

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
                message="Unable to determine export filename.",
                ok_action=renpy.store.Hide(),
            )
            return

        img_export_file = os.path.join(export_dir, export_filename)
        if os.path.exists(img_export_file):
            renpy.show_screen(
                "dialog",
                message="This image has already been exported.",
                ok_action=renpy.store.Hide(),
            )
            return

        with open(img_export_file, "wb") as outfile:
            outfile.write(renpy.open_file(renpy_img).read())

        renpy.show_screen(
            "dialog",
            message="Image exported to the 'gallery' folder in the base directory.",
            ok_action=renpy.store.Hide(),
        )


class GalleryAltImage(GalleryBase):
    """
    A class representing an alternative gallery image.
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
    A class representing a gallery image with additional attributes.
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
        Checks if the gallery image has alternative images.
        """
        return len(self.alts) > 0

    def unlock_alt_image(self, img_index: int) -> None:
        """
        Unlocks a specific alternative image for viewing.
        """
        if 0 <= img_index < len(self.alts):
            self.alts[img_index].unlock()

    def unlock_all_alt_images(self) -> None:
        for alt in self.alts:
            alt.unlock()

    def lock_alt_image(self, img_index: int) -> None:
        """
        Locks a specific alternative image, preventing viewing.
        """
        if 0 <= img_index < len(self.alts):
            self.alts[img_index].lock()

    def lock_all_alt_images(self) -> None:
        for alt in self.alts:
            alt.lock()


class GalleryDB:
    """
    A class to manage a database of gallery images.
    """

    def __init__(self):
        self.images: list[GalleryImage] = []
        self.image_index: int = 0
        self.alt_index: int = 0

    def add_image(self, image: GalleryImage) -> None:
        self.images.append(image)

    def set_image_index(self, index: int) -> None:
        if 0 <= index < len(self.images):
            self.image_index = index
            self.alt_index = 0

    def get_alt_image_index(self) -> int:
        return self.alt_index

    def set_alt_image_index(self, index: int) -> None:
        try:
            image = self.get_image()
            if 0 <= index < len(image.alts):
                self.alt_index = index
        except IndexError:
            raise IndexError("Invalid image index; cannot set alternative image index.")

    def get_image(self) -> GalleryImage:
        if len(self.images) == 0:
            raise IndexError("No gallery images available.")
        try:
            return self.images[self.image_index]
        except IndexError:
            raise IndexError("Invalid image index.")

    def get_alt_image(self) -> GalleryAltImage:
        image = self.get_image()
        if len(image.alts) == 0:
            raise IndexError("No alternative images available for this gallery image.")
        try:
            return image.alts[self.alt_index]
        except IndexError:
            raise IndexError("Invalid alternative image index.")

    def has_next_image(self) -> bool:
        return len(self.images) > 0 and self.image_index < len(self.images) - 1

    def has_prev_image(self) -> bool:
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
        Finds the next unlocked image from the current index.
        :return: The index of the next unlocked image, or None if none found.
        """
        if len(self.images) == 0:
            return None

        # Search forward from the current index.
        for i in range(self.image_index + 1, len(self.images)):
            if self.images[i].is_unlocked():
                return i

        # Wrap around and search from the beginning.
        for i in range(0, self.image_index + 1):
            if self.images[i].is_unlocked():
                return i

        return None

    def _find_prev_unlocked(self) -> int | None:
        """
        Finds the previous unlocked image from the current index.
        :return: The index of the previous unlocked image, or None if none found.
        """
        if len(self.images) == 0:
            return None

        # Search backward from the current index.
        for i in range(self.image_index - 1, -1, -1):
            if self.images[i].is_unlocked():
                return i

        # Wrap around and search from the end.
        for i in range(len(self.images) - 1, self.image_index - 1, -1):
            if self.images[i].is_unlocked():
                return i

        return None

    def _find_next_alt_unlocked(self) -> int | None:
        """
        Finds the next unlocked alternative image from the current alt index.
        :return: The index of the next unlocked alternative image, or None if none found.
        """
        try:
            image = self.get_image()
        except IndexError:
            return None

        if len(image.alts) == 0:
            return None

        # Search forward from the current alt index.
        for i in range(self.alt_index + 1, len(image.alts)):
            if image.alts[i].is_unlocked():
                return i

        # Wrap around and search from the beginning.
        for i in range(0, self.alt_index + 1):
            if image.alts[i].is_unlocked():
                return i

        return None

    def _find_prev_alt_unlocked(self) -> int | None:
        """
        Finds the previous unlocked alternative image from the current alt index.
        :return: The index of the previous unlocked alternative image, or None if none found.
        """
        try:
            image = self.get_image()
        except IndexError:
            return None

        if len(image.alts) == 0:
            return None

        # Search backward from the current alt index.
        for i in range(self.alt_index - 1, -1, -1):
            if image.alts[i].is_unlocked():
                return i

        # Wrap around and search from the end.
        for i in range(len(image.alts) - 1, self.alt_index - 1, -1):
            if image.alts[i].is_unlocked():
                return i

        return None

    def next_image(self) -> None:
        """
        Gets the next image in the gallery that is unlocked.
        """
        next_index = self._find_next_unlocked()
        if next_index is not None:
            self.image_index = next_index
            self.alt_index = 0

    def prev_image(self) -> None:
        """
        Gets the previous image in the gallery that is unlocked.
        """
        prev_index = self._find_prev_unlocked()
        if prev_index is not None:
            self.image_index = prev_index
            self.alt_index = 0

    def next_alt_image(self) -> None:
        """
        Gets the next alternative image for the current gallery image that is unlocked.
        """
        next_index = self._find_next_alt_unlocked()
        if next_index is not None:
            self.alt_index = next_index

    def prev_alt_image(self) -> None:
        """
        Gets the previous alternative image for the current gallery image that is unlocked.
        """
        prev_index = self._find_prev_alt_unlocked()
        if prev_index is not None:
            self.alt_index = prev_index

    def reset_navigation(self) -> None:
        self.image_index = 0
        self.alt_index = 0

    def get_images(self) -> list[GalleryImage]:
        return self.images

    def get_image_count(self) -> int:
        return len(self.images)


gallery_db = GalleryDB()
residential = GalleryImage("bg residential_day", unlock_by_default=True)
s1a = GalleryImage("sayori 1", sprite=True, unlock_by_default=True)
m1a = GalleryImage("monika 1", name="Monika", artist="Satchely", sprite=True)

gallery_db.add_image(residential)
gallery_db.add_image(s1a)
gallery_db.add_image(m1a)

for img in gallery_db.get_images():
    if img.is_unlocked():
        img.small_img
