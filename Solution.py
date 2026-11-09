
import heapq
import bisect

class Solution:
    def busiestServers(self, k, arrival, load):

        available = list(range(k))
        busy = []

        count = [0] * k

        for i in range(len(arrival)):

            current_time = arrival[i]

            # Release servers that have finished their requests
            while busy and busy[0][0] <= current_time:
                end_time, server = heapq.heappop(busy)

                bisect.insort(available, server)

            # If no server is available, drop the request
            if not available:
                continue

            # Find the preferred server
            preferred = i % k

            # Find the first available server >= preferred
            pos = bisect.bisect_left(available, preferred)

            # Circular search
            if pos == len(available):
                pos = 0

            server = available.pop(pos)

            # Update request count
            count[server] += 1

            # Mark server as busy
            end_time = current_time + load[i]

            heapq.heappush(busy, (end_time, server))

        # Find maximum handled requests
        maximum = max(count)

        # Return all servers with maximum requests
        return [
            i for i in range(k)
            if count[i] == maximum
        ]
