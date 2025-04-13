class Solution:
    def reorganizeString(self, s: str) -> str:

        # done (4/13/25)(Sun)(1240 to 120pm),(431/440-445pm)
        
        count = Counter(s) # makes a frequency counter for all the chars in the string
        n = len(s)

        # section 2: check if any of the max frequencies exceed (n+1)/2
        max_freq = 0
        for key, val in count.items():
            max_freq = max(max_freq, val)
        # first exit condition
        if max_freq > (n+1)//2:
            return ""
        
        #now construct the heap to then assemble the reorganized string
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)

        # this is the part I need to understand, how do you construct the string using the push and pop of the heap
        result = []
        prev_char, prev_freq = "", 0
        while heap:
            freq1, char1 = heapq.heappop(heap)
            result.append(char1)

            if prev_freq < 0: #max heap in python takes advantage of the min heap (-) property
                heapq.heappush(heap, (-prev_freq, prev_char))

            prev_freq = freq1+1
            prev_char = char1

        return "".join(result)