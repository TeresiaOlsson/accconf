"""
Base backend database options.
"""

# TODO: add function find based on search criteria and wildcards

import logging
from collections.abc import Generator
from typing import Any, Optional
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


ItemData = dict[str, Any]
ItemDataGen = Generator[ItemData, None, None]


class ConfigBackend(ABC):
    """
    Base class for backend database.
    """

    @property
    @abstractmethod
    def items(self) -> list[ItemData]:
        """List all items in the database

        Returns
        -------
        list[ItemData]
            List of item data in the database.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[ItemData]:
        """Get item by identifier.

        Parameters
        ----------
        id : str
            Identifier of item.

        Returns
        -------
        Optional[ItemData]
            Data for item.
        """
        pass     

    @abstractmethod
    def save(self,
             id: str,
             data: dict[str, Any],
             insert: bool = True) -> None:
        """Save data to the database.

        Parameters
        ----------
        id : str
            Identifier of item.
        data : dict[str, Any]
            Data to put into the database.
        insert : bool, optional
            Insert a new item in the database, by default True.
        """
        pass   

    @abstractmethod
    def delete(self, id: str) -> None:
        """Delete an item from the database.

        Parameters
        ----------
        id : str
            Identifier of item.
        """
        pass
