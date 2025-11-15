import heapq

pq = [5, 20, 1, 30, 4]
# prepares heap sorted (priority queue arr)
heapq.heapify(pq)  # [1, 4, 5, 30, 20]
print(pq)

# push a new element into priority queue
heapq.heappush(pq, 3)  # [1, 4, 3, 30, 20, 5]
print(pq)

# pop the top most element
print(heapq.heappop(pq))
print(pq)

# get n largest elements from priority queue
print(heapq.nlargest(2, pq))

# get n smallest elements from priority queue
print(heapq.nsmallest(2, pq))

# push & pop
print(heapq.heappushpop(pq, 2))
print(pq)

# push & pop [2.]
print(heapq.heappushpop(pq, 0))
print(pq)

# replace root item in the priority queue
print(heapq.heapreplace(pq, -1))
