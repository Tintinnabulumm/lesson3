#遍历整个列表
magicians = ['alice','david','caroline']
for magician in magicians:
    print(magician.title() + ' , that was a great trick!' )
print('nice job everyone!') #没有缩进的代码都只执行一次
#练习
animals = ['dog','cat','giraffe']
for animal in animals:
    print('a '+ animal + ' is a good pet')
print('any of these animals make a great pet')

#创建数值列表
for value in range(1,6):
    print(value) #从1开始，到6之前结束

#用range()创造数字列表
numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2)) #第三位是指步长，既前后两个数字之间的差
print(even_numbers)

#创造一个一串数的平方的列表
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#练习
numbers = list(range(1,21))
for number in numbers:
    print(number)

print(max(numbers)) #输出列表的最大值，最小值和总和
print(min(numbers))
print(sum(numbers))

#切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3]) #从列表的第一项开始，直到第四项之前结束
#如果是从开头开始，可以写成[:3]，如果是到末尾，可以写成[1:]，如果是整个都要，可以写成[:]

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#元组用()表示，是不可更改的
foods = ('pizza,','ice cream','salad','milktea','chicken')
for food in foods:
    print(food)
foods = ('tea','duck','salad','milktea','chicken')
for food in foods:
    print(food)