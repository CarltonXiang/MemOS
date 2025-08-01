from abc import ABC, abstractmethod
from typing import Any

from memos.configs.mem_reader import BaseMemReaderConfig
from memos.memories.textual.item import TextualMemoryItem


class BaseMemReader(ABC):
    """MemReader interface class for reading information."""

    @abstractmethod
    def __init__(self, config: BaseMemReaderConfig):
        """Initialize the MemReader with the given configuration."""

    @abstractmethod
    def get_scene_data_info(self, scene_data: list, type: str) -> list[str]:
        """Get raw information related to the current scene."""

    @abstractmethod
    def get_memory(
        self, scene_data: list, type: str, info: dict[str, Any]
    ) -> list[list[TextualMemoryItem]]:
        """Various types of memories extracted from scene_data"""

    @abstractmethod
    def transform_memreader(self, data: dict) -> list[TextualMemoryItem]:
        """Transform the memory data into a list of TextualMemoryItem objects."""
