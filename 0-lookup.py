"""Defines an object attribute lookup function"""


def lookup(hana):
    """Return a list of an object's available attributes"""
    return (dir(hana))
