"""Module for ItemTypes and the registry."""

import logging
from typing import Optional
from collections.abc import Generator
from .item import BaseItem

logger = logging.getLogger(__name__)

DEFAULT_REGISTRY = {"BaseItem": BaseItem}


class ConfigRegistry:
    """
    Registry of ItemTypes.

    The registry maps the full ItemType names to their class which is a subclass of BaseItem.
    """

    _loaded: bool
    _registry: dict[str, type[BaseItem]]

    def __init__(self):

        self._loaded = False
        self._registry = {}
    
    def load(self) -> None:
        """
        Load entries into the Registry.
        """

        # Add classes defined in DEFAULT_REGISTRY
        for name, cls in DEFAULT_REGISTRY.items():
            if name not in self._registry:
                self._registry[name] = cls

        # TODO: loading of entrypoints

        self._loaded = True   

    def __getitem__(self, item: str) -> Optional[type[BaseItem]]:

        if not self._loaded:
            self.load()
        try:
            return self._registry[item]
        except KeyError:
            raise KeyError(f"{item!r} not found in registry")
        
    def __contains__(self, item: str) -> bool:

        if not self._loaded:
            self.load()
        return item in self._registry

    def items(self) -> Generator[tuple[str, type[BaseItem]], None, None]:
        """All (item_name, item_class) entries in the registry."""

        if not self._loaded:
            self.load()
        yield from self._registry.items()

    def __setitem__(self, item: str, cls: type[BaseItem]) -> None:
        self._add(item, cls)

    def _add(self, key: str, cls: type[BaseItem]):
         
        # Get class in registry if the key already exists
        class_in_registry = self._registry.get(key, None)
         
        # Do nothing if the existing class in the registry is the same
        if class_in_registry is cls:
            return
         
        # Raise an error if the class exists but is not the same
        if class_in_registry is not None:
            raise RuntimeError(f"Duplicated entry found for key: {key} "
                               f"and class: {cls} {class_in_registry}") 

        # Everything is fine so add to registry
        self._registry[key] = cls
        
    
registry = ConfigRegistry()