# conveniences.py
import math
from nose.tools import assert_equal
nose.tools.assert_raises(OverflowError, math.log, 0)
nose.tools.assert_raises(ValueError, math.sqrt, -1)
# No equivalent for third example!
