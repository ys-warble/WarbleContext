import os

from WarbleContext import settings

if not os.path.exists(settings.RESOURCES_PATH):
    os.mkdir(settings.RESOURCES_PATH)

if not os.path.exists(settings.RAW_OUTPUT_PATH):
    os.mkdir(settings.RAW_OUTPUT_PATH)

if not os.path.exists(settings.PROCESSED_OUTPUT_PATH):
    os.mkdir(settings.PROCESSED_OUTPUT_PATH)
