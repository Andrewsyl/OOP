stuff = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
         'Kenneth Love': ['Python Basics', 'Python Collections', ]}

most_class = ''
counter = 0
for i in stuff:
    if len(stuff[i]) > counter:
        counter = len(stuff[i])
        most_class = i
print most_class


def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums) - 1):
        if i == 13:
            nums.remove(nums[i:i + 1])
    print sum(nums)


sum13([1, 2, 13, 2, 1, 13])
