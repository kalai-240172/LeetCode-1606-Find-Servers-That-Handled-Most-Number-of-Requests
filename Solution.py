import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """

        available = []
        busy = []
        result = []

        for index, weight in enumerate(servers):
            heapq.heappush(available, (weight, index))

        current_time = 0

        for i, task_time in enumerate(tasks):

            current_time = max(current_time, i)

            while busy and busy[0][0] <= current_time:
                finish_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:

                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    finish_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            result.append(index)

            finish_time = current_time + task_time

            heapq.heappush(
                busy,
                (finish_time, weight, index)
            )

        return result
