```python
a=10
b=20
print(a)
print(b)
print(a,b)
print(a,',',b)
```

    10
    20
    10 20
    10 , 20
    


```python
a=20
b=30
c=a+b
print(a-b)
print(c)
```

    -10
    50
    

# Print statement With String


```python
num1=50
num2=50
add=num1+num2
print('The addition of',num1,'and',num2,'is',add)
```

    The addition of 50 and 50 is 100
    


```python
name='Raviteja Beri.'
age='24'
place='Hyderabad,'
state='Telangana.'
occupation='Software Engineer.'
interest='Cricket.'
print('My name is',name,'And iam',age,'years old.','I live in',place,state,'Iam a',occupation,'My interest is',interest)
```

    My name is Raviteja Beri. And iam 24 years old. I live in Hyderabad, Telangana. Iam a Software Engineer. My interest is Cricket.
    


```python
num1=100 
num2=25 
num3=333 
avg=round((num1+num2+num3)/3,2) # or we can use avg=round(num1+num2+num3)/3,2) 
# The avrage of num1,num2,num3 is = avg 
print(f'The avrage of {num1}, {num2} and {num3} is = {avg}')
```

    The avrage of 100, 25 and 333 is = 152.67
    

# print with "End statement"


```python
print('Hello',end=' ')
print('good morning!')
```

    Hello good morning!
    


```python
print('Hello',end=', ')
print('good morning!')
```

    Hello, good morning!
    

# print with "Seperator "


```python
print('one','two','three','four',sep='-->')
```

    one-->two-->three-->four
    


```python
print('Raviteja ','VITS College ','Guntur ', sep='@ ')
```

    Raviteja @ VITS College @ Guntur 
    


```python

```
