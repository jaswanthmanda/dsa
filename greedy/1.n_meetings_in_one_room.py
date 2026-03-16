# N meetings in one room


class Solution:
    def maxMeetings(self, start, end):
        # your code goes here

        meetings = []
        for i, j in zip(start, end):
            meetings.append((i, j))

        meetings.sort(key=lambda x: x[1])

        last_time = float("-inf")
        counter = 0
        for i, j in meetings:
            if last_time < i:
                counter += 1
                last_time = j

        return counter
