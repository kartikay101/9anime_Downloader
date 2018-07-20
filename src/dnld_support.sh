# @Author: Kartikay Shandil <kartikay101>
# @Date:   2018-07-20T14:41:44+05:30
# @Last modified by:   kartikay101
# @Last modified time: 2018-07-20T20:42:41+05:30

#!/bin/bash
eval "uget-gtk --category-index="$1" --quiet --filename="\"$2\""  "$3""
