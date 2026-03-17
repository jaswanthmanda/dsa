# Job sequencing problem


class Solution:
    def JobScheduling(self, Jobs):
        # your code goes here
        # Sort jobs based on profit in descending order
        Jobs.sort(key=lambda x: x[2], reverse=True)

        # Total number of jobs
        n = len(Jobs)

        # Get the maximum deadline to complete the jobs
        maxDeadline = -1
        for it in Jobs:
            maxDeadline = max(maxDeadline, it[1])

        # Initialize a hash table to store selected jobs
        hash = [-1] * (maxDeadline + 1)

        # Initialize count
        cnt = 0

        # Initialize the total profit earned
        totalProfit = 0

        # Iterate over each job
        for i in range(n):
            """
            Iterate over each deadline slot
            starting from the job's deadline
            """
            for j in range(Jobs[i][1] - 1, -1, -1):
                # If the current deadline slot is available
                if hash[j] == -1:
                    cnt += 1  # Count of selected jobs
                    hash[j] = Jobs[i][0]  # Mark the job selected
                    totalProfit += Jobs[i][2]  # Update the total profit

                    # Move to the next job
                    break

        # Return the list
        return [cnt, totalProfit]
