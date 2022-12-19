
from enum import Enum


class TagType(str, Enum):
  ARTIST = "0"
  SERIES = "1"
  CHARACTOR = "2"
  ATTRIBUTE = "3"
  LANGUAGE = "4"
  EXTRA = "5"