class PuzzleLocked(Exception):
    """Raised when data from a locked puzzle was attempted to be fetched."""

    pass


class NoToken(Exception):
    """Raised when the session token was not found in the environment variables."""
