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
import time
import psutil
import os
from basic_sort_UNIQUE_SUFFIX import int_sort


def is_sorted(int_list):
    return all(int_list[i] <= int_list[i + 1] for i in range(len(int_list) - 1))


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5).tolist()]


def test_bubble(int_lists):
    process= psutil.Process()
    for lst in int_lists:
        #Measure CPU Usage before sorting
        cpu_start= process.cpu_times().user + process.cpu_times().system
        
        # Run bubble sort
        sorted_lst = int_sort.bubble(lst.copy())
        # Measure CPU Usage after sorting
        cpu_end= process.cpu_times().user + process.cpu_times().system
        cpu_time= cpu_end - cpu_start

        # print results
        print(f"\nInput list: {lst}")
        print(f"Sorted list: {sorted_lst}")
        print(f"CPU time: {cpu_time:.6f} seconds")
        
        assert is_sorted(sorted_lst), f"bubble sort failed on {lst}"


def test_quick(int_lists):
    process = psutil.Process()
    for lst in int_lists:
        # Record runtime at start
        realtime_start = time.perf_counter()
        cpu_timer_start = process.cpu_times()
        cpu_start = cpu_timer_start.user + cpu_timer_start.system

        # Run quicksort
        sorted_lst = int_sort.quick(lst.copy())

        # Record runtime at finish
        realtime_end = time.perf_counter()
        cpu_timer_end = process.cpu_times()
        cpu_end = cpu_timer_end.user + cpu_timer_end.system

        # print results
        real_time = realtime_end - realtime_start
        cpu_time = cpu_end - cpu_start
        print(f"\nInput list: {lst}")
        print(f"Sorted list: {sorted_lst}")
        print(f"Real time: {real_time:.6f} seconds")
        print(f"CPU time: {cpu_time:.6f} seconds")

        assert is_sorted(sorted_lst), f"quick sort failed on {lst}"


def test_insertion(int_lists):
    process = psutil.Process(os.getpid())
    for lst in int_lists:
        # Begin tracking memory usage
        mem_info = process.memory_info()
        mem_before = mem_info.rss

        # Run insertion sort
        sorted_lst = int_sort.insertion(lst.copy())

        # Record memory usage at finish
        mem_info = process.memory_info()
        mem_after = mem_info.rss

        print(f"\nInput list : {lst}")
        print(f"Sorted list: {sorted_lst}")
        print(f"Memory usage: {mem_after - mem_before}")
        
        assert is_sorted(sorted_lst), f"insertion sort failed on {lst}"
