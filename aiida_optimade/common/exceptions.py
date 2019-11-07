__all__ = (
    "AiidaEntityNotFound",
    "DeductionError",
    "OptimadeIntegrityError",
    "CausationError",
)


class AiidaEntityNotFound(Exception):
    """Could not find an AiiDA entity in the DB."""


class DeductionError(Exception):
    """Cannot deduce the value of an attribute."""


class OptimadeIntegrityError(Exception):
    """A required OPTiMaDe attribute or sub-attribute may be missing.
    Or it may be that the internal data integrity is violated,
    i.e., number of "species_at_sites" does not equal "nsites"
    """


class CausationError(Exception):
    """Cause-and-effect error, something MUST be done before something else is possible."""
