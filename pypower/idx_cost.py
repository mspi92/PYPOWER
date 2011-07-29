# Copyright (C) 1996-2011 Power System Engineering Research Center
# Copyright (C) 2010-2011 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Defines constants for named column indices to gencost matrix.

Some examples of usage, after defining the constants using the line above,
are::

    start = gencost[3, STARTUP]       # get startup cost of generator 4
    gencost[2, [MODEL, NCOST:COST+2]] = [POLYNOMIAL, 2, 30, 0]
    # set the cost of generator 2 to a linear function COST = 30 * Pg

The index, name and meaning of each column of the gencost matrix is given
below:

columns 1-5
    1.  C{MODEL}       cost model, 1 - piecewise linear, 2 - polynomial
    2.  C{STARTUP}     startup cost in US dollars
    3.  C{SHUTDOWN}    shutdown cost in US dollars
    4.  C{NCOST}       number of cost coefficients to follow for polynomial
    cost function, or number of data points for piecewise linear
    5.  C{COST}        1st column of cost parameters
    cost data defining total cost function
    For polynomial cost (highest order coeff first)::
        e.g. cn, ..., c1, c0
    where the polynomial is C{c0 + c1*P + ... + cn*P^n}
    For piecewise linear cost::
        x0, y0, x1, y1, x2, y2, ...
    where C{x0 < x1 < x2 < ...} and the points C{(x0,y0), (x1,y1),
    (x2,y2), ...} are the end- and break-points of the total cost function.

additional constants, used to assign/compare values in the C{MODEL} column
    1.  C{PW_LINEAR}   piecewise linear generator cost model
    2.  C{POLYNOMIAL}  polynomial generator cost model

@author: Ray Zimmerman (PSERC Cornell)
@author: Richard Lincoln
"""
# define cost models
PW_LINEAR   = 1
POLYNOMIAL  = 2

# define the indices
MODEL       = 0
STARTUP     = 1
SHUTDOWN    = 2
NCOST       = 3
COST        = 4
