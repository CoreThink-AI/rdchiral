import rdkit
from rdkit import RDLogger

from rdchiral import bonds

lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)

if rdkit.__version__ < '2019':
    raise ImportWarning('RDKit version {} may not be compatable with rdchiral. Upgrade to RDKit version 2019 or higher.'.format(rdkit.__version__))


__all__ = ["bonds"]
