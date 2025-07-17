
# 0imports.rpy
# This file imports certain python modules at runtime for DDLC and template
# features.

init -1 python:
    # Achievements/Gallery
    try:
        from store.achievements import achievementList, Achievement, AchievementCount
    except ModuleNotFoundError:
        pass
    
    try:
        from store.gallery import GalleryImage, galleryList
    except ModuleNotFoundError:
        pass