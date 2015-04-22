import pathFind
from gen_arena import arena
import test_lists


ar = arena("Tokyo", [])

path = pathFind.djistras(ar, [(1,1),(2,4)])
