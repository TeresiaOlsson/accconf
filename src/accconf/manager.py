"""Module for the manager."""

import logging
from .backends import DEFAULT_BACKEND
from .errors import DatabaseError, EntryError

logger = logging.getLogger(__name__)

class ConfigManager:
    """Client to manage the configuration database."""

    # Set that the key to use for the id should be name
 #   _id_key = 'name' 

    def __init__(self, database=None, **kwargs):

        # Use the database in the init
        if database:
            self.backend = database
            # TODO: add check so actually is a database

        # Load default database
        else:
            logger.debug("No database given, using '%s'", DEFAULT_BACKEND)
            try:
                self.backend = DEFAULT_BACKEND(**kwargs)
            except Exception as exc:
                raise DatabaseError(
                    f"Failed to instantiate a {DEFAULT_BACKEND} backend"
                ) from exc
            
    def _store(self, item, insert=False):
        """
        Store a document in the database.
        """

        logger.debug('Loading an item into the collection ...')

        # Validate item is ready for storage
        #self._validate_item(item)

        # Get the info for the item
        info = item.to_dict()

        # Get the existing if if the item is already in the database
#        old_name = info.get('_id', None)

        # Find id
        try:
            name = info['name']
        except KeyError:
            raise EntryError('Item did not supply the proper information '
                             'to interface with the database, missing name')
        
        # TODO: add handling of changing the name

        logger.info('Adding / Modifying information for %s ...', name)
        self.backend.save(name, info, insert=insert)
        return name

        
        # # In case we want to update the name of an entry
        # # we want to add a new entry, and delete the old one
        # if old_name and old_name != info[self._id_key]:
        #     # Store information for the new entry
        #     logger.info('Saving new entry %s ...', _id)
        #     self.backend.save(_id, post, insert=True)
        #     # Remove the information for the old entry
        #     logger.info('Removing old entry %s ...', the_old_name)
        #     self.backend.delete(the_old_name)
        # else:
        #     # Store information
        #     logger.info('Adding / Modifying information for %s ...', _id)
        #     self.backend.save(_id, post, insert=insert)
        return _id            
            

    def add_item(self, item) -> str:
        """Add an item into the database."""

        logger.info("Storing item %r ...", item)

        name = self._store(item, insert=True)
        logger.info(
            "Item %r has been succesfully added to the database",
            item
        )
        return name            
