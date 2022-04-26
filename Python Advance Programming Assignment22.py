#!/usr/bin/env python
# coding: utf-8

# 1. Create a class Smoothie and do the following:
# - Create an instance attribute called ingredients.
# - Create a get_cost method which calculates the total cost of the
# ingredients used to make the smoothie.
# - Create a get_price method which returns the number from get_cost plus
# the number from get_cost multiplied by 1.5. Round to two decimal places.
# - Create a get_name method which gets the ingredients and puts them in
# alphabetical order into a nice descriptive sentence. If there are multiple
# ingredients, add the word &quot;Fusion&quot; to the end but otherwise, add &quot;Smoothie&quot;.
# Remember to change &quot;-berries&quot; to &quot;-berry&quot;. See the examples below.
# Ingredient Price
# Strawberries $1.50
# Banana $0.50
# Mango $2.50
# Blueberries $1.00
# Raspberries $1.00
# Apple $1.75
# Pineapple $3.50
# Examples
# s1 = Smoothie([&quot;Banana&quot;])
# s1.ingredients ➞ [&quot;Banana&quot;]
# s1.get_cost() ➞ &quot;$0.50&quot;
# s1.get_price() ➞ &quot;$1.25&quot;
# s1.get_name() ➞ &quot;Banana Smoothie&quot;
# s2 = Smoothie([&quot;Raspberries&quot;, &quot;Strawberries&quot;, &quot;Blueberries&quot;])
# s2.ingredients ➞ [&quot;Raspberries&quot;, &quot;Strawberries&quot;, &quot;Blueberries&quot;]
# s2.get_cost() ➞ &quot;$3.50&quot;
# s2.get_price() ➞ &quot;$8.75&quot;
# s2.get_name() ➞ &quot;Blueberry Raspberry Strawberry Fusion&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


import re
class Smoothie:
    ingredients_price = {
        'Strawberries':1.50,
        'Banana':0.50,
        'Mango':2.50,
        'Blueberries':1.00,
        'Raspberries':1.00,
        'Apple':1.75,
        'Pineapple':3.50
    }
    def __init__(self,ingredients):
        self.ingredients = ingredients
        self.cost = 0
    def get_cost(self):
        for ele in self.ingredients:
            if ele in Smoothie.ingredients_price:
                self.cost += round(Smoothie.ingredients_price.get(ele,0),2)
        return '$'+str(self.cost)
    def get_price(self):
        self.price = round((self.cost*1.5)+(self.cost),2)
        return '$'+str(self.price)
    def get_name(self):
        self.name = re.sub('berries','berry',' '.join(sorted(self.ingredients)))
        self.name = self.name+' Smoothie' if len(self.ingredients) == 1 else self.name+' Fusion'
        return self.name

s1 = Smoothie(["Banana"])
print(f's1.ingredients ➞ {s1.ingredients}')
print(f's1.get_cost() ➞ "{s1.get_cost()}"')
print(f's1.get_price() ➞ "{s1.get_price()}"')
print(f's1.get_name() ➞ "{s1.get_name()}"')

s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
print(f's2.ingredients ➞ {s2.ingredients}')
print(f's2.get_cost() ➞ "{s2.get_cost()}"')
print(f's2.get_price() ➞ "{s2.get_price()}"')
print(f's2.get_name() ➞ "{s2.get_name()}"')


# 2. Your task is to write a program which allows teachers to create a multiple
# choice test in a class called Testpaper and to be also able to assign a
# minimum pass mark. The testpaper&#39;s subject should also be included. The
# attributes are in the following order:
# 1. subject
# 2. markscheme
# 3. pass_mark
# As well as that, we need to create student objects to take the test itself!
# Create another class called Student and do the following:
# - Create an attribute called tests_taken and set the default as &#39;No tests
# taken&#39;.
# - Make a method called take_test(), which takes in the testpaper object they
# are completing and the student&#39;s answers. Compare what they wrote to the
# mark scheme, and append to the/create a dictionary assigned to tests_taken
# in the way as shown in the point below.
# - Each key in the dictionary should be the testpaper subject and each value
# should be a string in the format seen in the examples below (whether or not
# the student has failed, and their percentage in brackets).
# Examples
# paper1 = Testpaper(&quot;Maths&quot;, [&quot;1A&quot;, &quot;2C&quot;, &quot;3D&quot;, &quot;4A&quot;, &quot;5A&quot;], &quot;60%&quot;)
# paper2 = Testpaper(&quot;Chemistry&quot;, [&quot;1C&quot;, &quot;2C&quot;, &quot;3D&quot;, &quot;4A&quot;], &quot;75%&quot;)
# paper3 = Testpaper(&quot;Computing&quot;, [&quot;1D&quot;, &quot;2C&quot;, &quot;3C&quot;, &quot;4B&quot;, &quot;5D&quot;, &quot;6C&quot;, &quot;7A&quot;],
# &quot;75%&quot;)
# student1 = Student()
# student2 = Student()
# student1.tests_taken ➞ &quot;No tests taken&quot;
# student1.take_test(paper1, [&quot;1A&quot;, &quot;2D&quot;, &quot;3D&quot;, &quot;4A&quot;, &quot;5A&quot;])
# student1.tests_taken ➞ {&quot;Maths&quot; : &quot;Passed! (80%)&quot;}
# student2.take_test(paper2, [&quot;1C&quot;, &quot;2D&quot;, &quot;3A&quot;, &quot;4C&quot;])
# student2.take_test(paper3, [&quot;1A&quot;, &quot;2C&quot;, &quot;3A&quot;, &quot;4C&quot;, &quot;5D&quot;, &quot;6C&quot;, &quot;7B&quot;])
# student2.tests_taken ➞ {&quot;Chemistry&quot; : &quot;Failed! (25%)&quot;, &quot;Computing&quot; : &quot;Failed!
# (43%)&quot;}
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


class Testpaper:
    def __init__(self,subject,markscheme,pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
        
class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"
    def take_test(self,paper_name,student_response):
        correct_responses = 0
        for ele in range(len(paper_name.markscheme)):
            if paper_name.markscheme[ele] == student_response[ele]:
                correct_responses +=1
        ach_pass_mark = int(correct_responses/len(paper_name.markscheme)*100)
        needed_pass_mark = int(paper_name.pass_mark.split("%")[0])
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {}
        if ach_pass_mark >= needed_pass_mark:
            self.tests_taken[paper_name.subject] = f"Passed! ({str(ach_pass_mark)}%)"
        else:
            self.tests_taken[paper_name.subject] = f'Failed! ({str(ach_pass_mark)}%)'
        
paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")  
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")  
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")       

student1 = Student()   
student2 = Student()

print(f'student1.tests_taken ➞ "{student1.tests_taken}"')
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(f'student1.tests_taken ➞ {student1.tests_taken}')

student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
print(f'student2.tests_taken ➞ {student2.tests_taken}')


# 3. Due to unforseen circumstances in Suburbia, the trains will be delayed by
# a further 10 minutes.
# 
# Create a function that will help to plan out and manage these delays! Create
# a function called manage_delays that does the following:
# - Parameters will be the train object, a destination and number of minutes
# the delay is.
# - Increment to the train object&#39;s expected_time by the delay, if the
# destination given is in the train object&#39;s destinations.
# Examples
# trains = [
# Train([&quot;Townsville&quot;, &quot;Suburbia&quot;, &quot;Urbantska&quot;], &quot;13:04&quot;),
# Train([&quot;Farmsdale&quot;, &quot;Suburbia&quot;, &quot;Lakeside Valley&quot;], &quot;13:20&quot;),
# Train([&quot;Suburbia&quot;, &quot;Townsville&quot;, &quot;Lakeside Valley&quot;], &quot;13:22&quot;)
# ]
# for t in trains:
# manage_delays(t, &quot;Lakeside Valley&quot;, 60)
# trains[0].expected_time ➞ &quot;13:04&quot;
# trains[1].expected_time ➞ &quot;14:20&quot;
# trains[2].expected_time ➞ &quot;14:22&quot;
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     
# Ans:-

# In[3]:


class Train:
    def __init__(self,destination_list,expected_time):
        self.destination_list = destination_list
        self.expected_time = expected_time

def manage_delays(train_obj,destination_point,delay):
    if destination_point in train_obj.destination_list:
        ex_time = train_obj.expected_time.split(":")
        new_ex_time = str((int(ex_time[0])*60+int(ex_time[1])+int(delay))//60)+':'+str((int(ex_time[0])*60+int(ex_time[1])+int(delay))%60)
        train_obj.expected_time = new_ex_time

trains = [
  Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
  Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
  Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
]

for t in trains:
    manage_delays(t, "Lakeside Valley", 60)
        
print(f'trains[0].expected_time ➞ "{trains[0].expected_time}"')    
print(f'trains[1].expected_time ➞ "{trains[1].expected_time}"')    
print(f'trains[2].expected_time ➞ "{trains[2].expected_time}"')    


# 4. Ted works as a computer programmer at Minecraft Inc. His boss has just
# given him an important assignment to update the code for the minecart tracks
# by the end of April. However, he has recently had to self-isolate due to
# Corvid-19 and has left the code for the tracks BACK AT WORK!! He has the
# shorthand for the tracks he&#39;s supposed to look at, and where the carts are
# suppost to end up, but not the actual code.
# He knows that:
# 1. &quot;--&gt;&quot; = &quot;Speed-Up Track&quot; ⁠— If a minecart interacts with this track, it&#39;s
# velocity increases by 2.67 BPS unless it&#39;s at its maximum speed of 8 BPS.
# 2. &quot;&lt;--&gt;&quot; = &quot;Powered Track&quot; ⁠— If a minecart interacts with this track, it&#39;s
# velocity remains the same.
# 3. &quot;&lt;--&quot; = &quot;Slow-Down Track&quot; ⁠— If a minecart interacts with this track, it&#39;s
# velocity decreases by 2.67 BPS unless it&#39;s velocity equals 0, at which point it
# stops.
# 4. &quot;---&quot; = &quot;Unpowered Track&quot; ⁠— If a minecart interacts with this track, it&#39;s
# velocity decreases by 1 BPS unless it&#39;s velocity equals 0, at which point it
# stops.
# 
# Help Ted by writing a class for the tracks that interact with the provided
# Minecart class as shown above. And then write a function that will take a list
# of the shorthand tracks and:
# - If the Minecart reaches the last peice of Track, return True.
# - Else return the index of the Track where the Minecart stops.
# Examples
# mine_run([&quot;--&gt;&quot;, &quot;--&gt;&quot;, &quot;--&gt;&quot;, &quot;&lt;--&quot;, &quot;&lt;--&quot;, &quot;&lt;--&quot;]) ➞ True
# mine_run([&quot;--&gt;&quot;, &quot;&lt;--&quot;, &quot;--&gt;&quot;, &quot;--&gt;&quot;, &quot;&lt;--&gt;&quot;, &quot;---&quot;]) ➞ 1
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


class minecraft:
    def __init__(self,tracks):
        self.tracks = tracks
        
def mine_run(tracks):
    mine_vel = 0  
    output = 0
    for ele in range(len(tracks)):
        if tracks[ele] == '-->':
            if mine_vel+2.67 >= 8: mine_vel = 8 # resetted to max mine_val
            else: mine_vel +=2.67
        elif tracks[ele] == '<-->': continue
        elif tracks[ele] == '<--':
            if mine_vel-2.67 <= 0: output = True if ele == len(tracks)-1 else ele; break
            else: mine_vel -=2.67
        else:
            if mine_vel-1 <= 0: output = True if ele == len(tracks)-1 else ele; break
            else: mine_vel -=1        
    return output

mine_track_1 = minecraft(["-->", "-->", "-->", "<--", "<--", "<--"])
print(f'mine_run({mine_track_1.tracks}) ➞ {mine_run(mine_track_1.tracks)}')
mine_track_2 = minecraft(["-->", "<--", "-->", "-->", "<-->", "---"])
print(f'mine_run({mine_track_2.tracks}) ➞ {mine_run(mine_track_2.tracks)}')


# 5. Make a Rectangle class with four parameters, an x, a y (representing the
# top-left corner of the rectangle), a width and a height exclusively in that order.
# Lastly, make a function intersecting that takes two Rectangle objects and
# returns True if those objects are intersecting (colliding), else return False.
# Examples
# a = Rectangle(10, 20, 100, 20)
# b = Rectangle(10, 40, 15, 20)
# c = Rectangle(50, 50, 20, 30)
# intersecting(a, b) ➞ True
# intersecting(a, c) ➞ False
# intersecting(b, c) ➞ True
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[6]:


def intersecting(rectangle1, rectangle2):
    output = False
    if (rectangle2.y-rectangle1.y == rectangle1.height) or (rectangle2.y-rectangle1.y + rectangle1.height == rectangle2.height):
        output = True
    print(f'intersecting{rectangle1.__dict__.values(),rectangle2.__dict__.values()} ➞ {output}')

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)
intersecting(a, b)
intersecting(a, c)
intersecting(b, c)

