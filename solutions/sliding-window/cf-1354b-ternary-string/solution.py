import sys

def check_if_valid(seen : list):
    for v in seen[1:]:
        if v == 0:
            return False
    return True 

def solve(s):
    # TODO: return the answer for one test case
    arr = [int(a) for a in list(s)]
    seen = [0]*4
    left = 0
    ans = float('inf')
    for right in range(len(arr)):
        seen[arr[right]] += 1
        if check_if_valid(seen):
            ans = min(ans, right-left+1)
            while left < right and (check_if_valid(seen)):
                seen[arr[left]]-=1
                ans = min(ans, right-left+1)
                left+=1
               

        



        
        
    return ans if float('inf') != ans else 0
    

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    for i in range(1,  t+1):
        out.append(str(solve(data[i])))
    print("\n".join(out))

main()