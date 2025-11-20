# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

import pytest
import numpy as np
from basic_sort_UNIQUE_SUFFIX import int_sort


def is_sorted(int_list):
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5).tolist()]


def test_bubble(int_lists):
    for lst in int_lists:
        sorted_lst = int_sort.bubble(lst.copy())
        assert is_sorted(sorted_lst), f"bubble sort failed on {lst}"


def test_quick(int_lists):
    for lst in int_lists:
        sorted_lst = int_sort.quick(lst.copy())
        assert is_sorted(sorted_lst), f"quick sort failed on {lst}"


def test_insertion(int_lists):
    for lst in int_lists:
        sorted_lst = int_sort.insertion(lst.copy())
        assert is_sorted(sorted_lst), f"insertion sort failed on {lst}"
