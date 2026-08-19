class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = {}

        # Store reserved seats of each row as a bitmask
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0
            rows[row] |= 1 << (seat - 1)

        ans = 0

        # Check only rows containing reserved seats
        for seats in rows.values():

            # Can place both:
            # Left  -> seats 2,3,4,5
            # Right -> seats 6,7,8,9
            left = 0b00000011110
            right = 0b0111100000

            if (seats & left) == 0 and (seats & right) == 0:
                ans += 2

            # Otherwise, check whether one group can fit
            elif ((seats & left) == 0 or
                  (seats & right) == 0 or
                  (seats & 0b0001111000) == 0):
                ans += 1

        # Rows with no reservations can always fit 2 families
        empty_rows = n - len(rows)
        ans += empty_rows * 2

        return ans
        