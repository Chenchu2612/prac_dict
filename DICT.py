1.
def sort_dict(d):
    return sorted(d.items(),key=lambda x:x[1],reverse=False)
print(sort_dict(eval(input("enter the dict"))))
d.items = for spliting the each key-value pair in a list of tuple
key=lambda x:x[n],here n=0 means key n=1 means value.
without lambda we can write a function and write key=function
reverse=False means sort ascending .....by default sort ascending
reverse=True means sort decending
eval function for what iterable in side the input those will take otherwise total iterable will take as string
dict={'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}

print(dict.items())
sorted based on value-desending
print(sorted(dict.items(),key=lambda x:x[1],reverse= True))
sorted based on value-ascending
print(sorted(dict.items(),key=lambda x:x[1],reverse=False))
sorted based on key-ascending
print(sorted(dict.items(),key=lambda x:x[0],reverse=False))
sorted based on key-decending
print(sorted(dict.items(),key=lambda x:x[0],reverse=True))

2.
d = {0:10, 1:20}  #three methods available
method 1 ---update with key value
d[2]=25
print(d)
method2---update with update method
d.update({2:25})
print(d)
method 3--update with set default method
d.setdefault(2,25)
print(d.setdefault(2,25))
print(d)

3.
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
d={}
d.update(dict1,dict2,dict3) # update method requried only one argument here we fave 3
print(d)
d.add(dict1) # dict dont have add method
print(d)
d=dict1+dict2+dict3 # dict dont have + operator method
print(d)
d=dict(dict1,dict2,dict3) # here dict() object need only one argument
print(d)
so for this we need loop:
for item in (dict1,dict2,dict3):   # this is correct order of adding------wrong order is----  for item  in (dict1,dict2,dict3):
   d.update(item)                                                                                  print(d.update(item)
print(d)

4.
x = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(d):
    if d in x.keys():             # in operator to check key exist or not---- we can provide x also by default it takes x.keys()
        print("the key is present")
    else:
        print("key is not present")
is_key_present(6)

def is_key_present(a):
    if a in x:
        print("true")
    else:
        print("false")
is_key_present(8)

with inbuilt
get method
print(x.get(8))
set default method
print(x.setdefault(8,9))
print(x)

5.
for key and value both
def iterate_dict(d):
    for k,v in d.items():      # for key and value both
        print(k,"---",v)
iterate_dict(eval(input("enter the dictionary:")))

only keys
mehod-1

def iterate_dict(d):
    for k in d.keys():  # only for keys
        print(k)
iterate_dict(eval(input("enter the dictionary:")))
#
method--2
#
def iterate_dict(d):
    for k in d:
        print(k)
iterate_dict(eval(input("enter the dictionary:")))
only values
def iterate_dict(d):
    for v in d.values():
        print(v)
print(iterate_dict(eval(input("enter the dictionary:"))))


6.
dict comp
def dict_comp(n):
    result={x:x*x for x in range(1,n+1)}   # range always excludes stop value  # x for key :x for value
    return result
print(dict_comp(int(input("enter the n value:"))))

normal method.
def normal(n):
    d={}
    for x in range(1,n+1):   # range always excludes stop value
        d[x]=x*x                  #d[x] is for key x*x for value
    return d
print(normal(int(input("enter the n value:"))))

7.
dict comp
def new_dict(a):
    result={x:x*x for x in range(1,a+1)}
    return result
print(new_dict(int(input("enter the a value:"))))


8.
inbuilt method
def add_dict(a,b):
    c=a.copy()   # copying a into c
    c.update(b)  # updating c with a
    return c
print(add_dict(eval(input("enter the dict a")),eval(input("enter the dict b"))))

without inbuilt
def add_dict(*dicts):
    new=dict()
    for d in dicts:
        new.update(d)
    return new
print(add_dict(eval(input("enter the dictionaries:"))))

9.
this is wrong method   XXXX
def iterate(d):
    for k,v in d.items():
        return (k,"--",d[k])     # here we will never put return inside loop if we put it  stops the iteration after execution of first loop
print(iterate(eval(input("enter the dictionary:"))))

correct method for k,v looping
def iterate_key_value(d):
    for k,v in d.items():        # if we give only d it will takes only keys.
        print(k,"--",k[v])
iterate_key_value(eval(input("enter the dict:")))

iterate only keys.
def iterate_key(d):
    for k in d:     # here we can give d.keys() also
        print(k)
iterate_key(eval(input("enter the dictionary:")))

iterate only values.
def iterate_values(d):
    for v in d.values():
        print(v)
iterate_values(eval(input("enter the dictionary:")))

another method:
def iterate_values(d):
    for a,v in d.items():    # here e can provide d.keys()
        print(d[a])
iterate_values(eval(input("enter the value:")))

10.  sum of all items in the dictionary.
method.1
def sum_items(a):
    sum_value=0
    for v in a.values():
        sum_value+=v
    return sum_value
print(sum_items(eval(input("enter the values:"))))

method.2
def sum_values(a):
    sum_val=0
    for k,v in a.items():
        sum_val+=a[k]           # here a[k] represent the value of key
    return sum_val
print(sum_values(eval(input("enter the dictionary:"))))

11.
method.1
def multiply(a):
    mul=1     # initilising multiply varible
    for v in a.values():
        mul=v*v
    return mul
print(multiply(eval(input("enter the dictionary:"))))

method.2

def multiply(a):
    mul=1    # initialising multiply varible
    for k,v in a.items():
        mul=mul*a[k]    # a[k] mens key value
    return mul
print(multiply(eval(input("enter the dict"))))

# 12.

wrong
def delete_key(dict):
    for key in dict:
        del dict[key]    # runtime error: it changed the size during iteration
    return dict
delete_key(eval(input("enter the dictionary:")))

correct method

def delete_key(dict):
    if "data2" in dict:
        del dict["data2"]   # it deletes the particular key
    return dict
print(delete_key(eval(input("enter the dictionary:"))))

13.
method 1 by using zip object
def dict_map(list1,list2):
    return dict(zip(list1,list2))
print(dict_map(eval(input("enter the list1")),eval(input("enter the list2"))))

method 2:
 by using for loop
def dict_map(list1,list2):
    dict={}
    for key in list1:
        for value in list2:
            dict[key]=value
            list2.remove(value)
            break
    return dict
print(dict_map(eval(input("enter the list1")),eval(input("enter the list2"))))

method.3
by using dictcomprehension (with the help of index)
def map_dict(list1,list2):
    return {str(list1[i]):str(list2[i]) for i in range(len(list1))}
print(map_dict(eval(input("enter the list1:")),eval(input("enter the list2:"))))

14.

def sorte_key(d):
    return dict(sorted(d.items(),key=lambda a:a[0],reverse=False))    #1.dict fo making dictionary 2.sorted for key value pair in tuple form,3.key is for based on witch position the sorted is starts,reverse for asending and decending purpose
print(sorte_key(eval(input("enter the dict:"))))

15.
def max_min(a):
    dict(sorted(a.items(),key=lambda x:x[1],reverse=False))
    result= max(dict.values())
    result2=min(dict.values())
    return result,result2
print(max_min(eval(input("enter the dictionry:"))))


15.
dict={"a":500,"b":600,"z":5}
key_max=(max(dict.keys(),key=(lambda a:dict[a]))) # manam ikkada lambda function lo value adharamga max kanukkomani cheppamu lednte adi key alphabatic order prakaram sort chestadi (max(dict.keys())
key_min=min(dict.keys(),key=(lambda a:dict[a]))
print(dict[key_max])
print(dict[key_min])

16.
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
chenchu=Student("ramu",25,96)
print(chenchu.__dict__)   # it returns the dict items with key value pairs.

17.

def remove_duplicates(d):
    dict = {}
    for key, value in d.items():  # here we are comparing  only values why we have to take keys also ? --> bcoz based on value we are adding key and value to the new dictionary ....if we are providing only value whie adding key to new dict interpreter will ask where is key like that ...
        if value not in dict:
            dict[key] = value
    return dict


print(remove_duplicates(eval(input("enter the dictionary:"))))

18.
def emepty_not(d):
    if not bool(d):   # bool returns True if a iterable contains elements...it returns False if an iterble is emepty
        print("the dictionary is emepty") # not reverse the result
emepty_not(eval(input("enter the dictionary")))

"CHENCHU""SIVA"

"hello" "hai"
