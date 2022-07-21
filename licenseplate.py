"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        str1 = str[:3]
        str2 = str[3:]
        count1 = 0
        count2 = 0
        count = 0
        for i in str1:
            if i == ".":
                count2 += 1
        for j in str2:
            if j == ".":
                count1 += 1

        if count1 >= 1:
            count += 10-(4-count1)
        if count1 >= 2:
            count *= 9-(4-count1)
        if count1 >= 3:
            count *= 8-(4-count1)
        if count1 >= 4:
            count *= 7-(4-count1)

        if count == 0 and count2 >= 1:
            count += 26-(3-count2)
        elif count2 >= 1:
            count *= 26-(3-count2)
        if count2 >= 2:
            count *= 25- (3-count2)
        if count2 >= 3:
            count *= 24- (3-count2)
        
        return count



def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()