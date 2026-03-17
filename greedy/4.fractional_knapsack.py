# Fractional Knapsack


class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        result = []

        for val_item, wt_item in zip(val, wt):
            # calc per unit
            k = val_item / wt_item
            result.append((val_item, wt_item, k))

        # sort in reverse per unit weight value
        result.sort(reverse=True, key=lambda x: x[2])

        ans = 0

        # now iterate and calculate the value
        for val_item, wt_item, k_item in result:
            if wt_item <= cap:
                cap -= wt_item
                ans += val_item
            elif cap != 0:
                fraction = cap / wt_item
                ans += fraction * val_item
                break

        return ans
