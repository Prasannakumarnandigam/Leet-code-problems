class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #step 1
        if not nums:
            return 0

        #step 2 -> start slow
        slow = 1

        #step 3 -> start fast in loop
        for fast in range(1, len(nums)):

            # Step 4: The Check
            # Compare the current number (fast) with the previous one (fast - 1).
            # Since the list is sorted, duplicates always sit next to each other

            if nums[fast] != nums[fast - 1]:

                # Step 5: The Overwrite
                # We found a unique number! Write it down at the 'slow' position.

                nums[slow] = nums[fast]

                # Step 6: Move the Writer
                # Get ready for the next unique number.

                slow = slow + 1

        return slow