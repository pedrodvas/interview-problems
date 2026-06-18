class Solution(object):
    def twoSum(self, nums, target):
        used_nums = set()
        complements = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if num in complements:
                return [complements[num], i]
            else:
                complements[complement] = i

            used_nums.add(num)
    
    def twoSum2(self, nums, target):
        sums = {}
        used_nums = set()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if num not in used_nums:

                if num in sums:
                    return [sums[num], i]
                else:
                    sums[num] = i

                if complement in sums and complement != num:
                    return [sums[complement], i]
                else:
                    sums[complement] = i
                
                used_nums.add(num)
    
    def twoSum1(self, nums, target):
        #solução < n
        #usa memória pra krl 64b*maior numero mais ou menos
        #só funciona para naturais
        #dá pra adaptar para negativos mas tenho preguiça
        biggest = nums[0]
        for i in range(len(nums)):
            if nums[i] > biggest:
                biggest = nums[i]

        sums = [[] for _ in range(biggest+1)]

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            sums[num].append(i)
            if len(sums[num]) > 1:
                return [sums[num][0], sums[num][1]]
            
            if complement != num:
                sums[complement].append(i)
                if len(sums[complement]) > 1:
                    return [sums[num][0], sums[num][1]]


        #também existe solução com n lgn, mas fiquei com
        #preguiça de fazer busca binaria pelo lugar certo
        #dessa forma usa menos memório que o jeito de cima

    def twoSum0(self, nums, target):
        #solução de n**2
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j] == target):
                        return [i, j]


if __name__ == '__main__':
    sol = Solution()
    sol.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], 11)