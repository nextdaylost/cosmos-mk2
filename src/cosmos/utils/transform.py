"""Value transformation utilities."""


def to_camel(in_str: str) -> str:
    """Converts a snake case string to a camel case string.

    Arguments:
        in_str: A snake case string.

    Returns:
        A camel case string.
    """
    str_parts = in_str.lstrip("_").split("_")
    return "".join([in_str[0], *[el.capitalize() for el in str_parts[1:]]])
