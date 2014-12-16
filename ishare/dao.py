from ishare.models import Album, Image

def get_user_albums(user, limit=20, order_by='last_modified_date'):
    """
    Get all albums of a user.

    Return: list a albums.
    """
    return Album.objects.filter(entity__creator=user).order_by(order_by)[:limit]

def get_recent_albums(limit=20, order_by='last_modified_date'):
    return Album.objects.order_by(order_by)[:limit]

def get_recent_images(limit=20, order_by='-entity__create_date'):
    return Image.objects.order_by(order_by)[:limit]

