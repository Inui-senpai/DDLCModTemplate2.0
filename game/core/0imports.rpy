# 0imports.rpy

# В этом файле прописаны импорты модулей Python, необходимых для
# необязательного функционала мод-шаблона.

init -1 python:
    # Достижения/Галерея
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ModuleNotFoundError:
        pass
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass