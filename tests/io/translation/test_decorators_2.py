from nagini_contracts.contracts import Predicate, Result
from nagini_contracts.io import *


#:: ExpectedOutput(invalid.program:decorators.incompatible)
@IOOperation
@Predicate
def read_int_io(
        t_pre1: Place,
        res: int = Result(),
        t_post: Place = Result(),
        ) -> bool:
    Terminates(False)
