from ishare.models import Album, Image

def get_user_albums(user, order_by='-last_modified_date'):
    """
    Get all albums of a user.

    Return: list a albums.
    """
    return Album.objects.filter(entity__creator=user).order_by(order_by)