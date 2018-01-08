""" This class is for storing or extracting information of photo objects """
class Photo():
    """ The Photo object is used to store photo infomation from flickr.
        It contains attributes:
            {
             'tags': the tags user has tagged the current photo,
             'description': the description of the current photo,
             'title': the title of current photo,
             'owner': the owner of the current photo,
             'date': the date of the current photo
            }
        It contains methods:
            {
             'get_tags': return all the tags of the current photo,
             'get_tags_number': return the number of tags of current photo,
            }
"""
    def __init__(self, photo_info):
        self.tags = [item['_content'] for item in photo_info['tags']['tag']]
        self.description = photo_info["description"]["_content"]
        self.title = photo_info["title"]["_content"]
        self.owner = photo_info["owner"]["username"]

    def get_tags(self):
        """ Return all tags of the photo if interested """
        return self.tags

    def get_tags_number(self):
        """ Return the number of tags of current photo """
        return len(self.tags)

    # Default method: __str__
    def __str__(self):
        return "This photo has tags {}". format(self.tags)

    def to_dict(self):
        """ Helper function to when converting object to dataframe """
        return {
            "title": self.title,
            "user": self.owner,
            "tags": self.tags,
            "num_of_tags": len(self.tags),
            "description": self.description,
        }
