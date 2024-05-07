class Solution:
    def toh(self, N, fromm, to, aux):
        # Base case: if there is only one disk to move
        if N == 1:
            print(f"Move disk 1 from rod {fromm} to rod {to}")
            return 1  # One move made

        # Recursive case: move N-1 disks from 'fromm' to 'aux', using 'to' as an auxiliary rod
        moves = 0
        moves += self.toh(N - 1, fromm, aux, to)  # Move N-1 disks to auxiliary rod

        # Move the N-th disk (the largest one) from 'fromm' to 'to'
        print(f"Move disk {N} from rod {fromm} to rod {to}")
        moves += 1  # Count this move

        # Move the N-1 disks from 'aux' to 'to', using 'fromm' as an auxiliary rod
        moves += self.toh(N - 1, aux, to, fromm)

        return moves  # Return the total number of moves

# Create an instance of Solution
s = Solution()
# Call the toh method and print the total moves
print(s.toh(3, 1, 3, 2))
