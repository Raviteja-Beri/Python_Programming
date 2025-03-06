# Tuple  
#### remember always use ()

### 1. Tuple Creation


```python
t=() # Empty tuple creation
t
```




    ()




```python
t1=(1,2,3) # integer numbers
t1
```




    (1, 2, 3)




```python
t2=(1.5,2.5,3.5,4.5,5.5) # float numbers
t2
```




    (1.5, 2.5, 3.5, 4.5, 5.5)




```python
t3=('ravi','beri','cpl') # string
t3
```




    ('ravi', 'beri', 'cpl')




```python
t4=(22,35,55,(65,34,57),(21,98)) # nested tuples
t4
```




    (22, 35, 55, (65, 34, 57), (21, 98))




```python
t5=(10,2.5,'ravi',3+5j) # All data types
t5
```




    (10, 2.5, 'ravi', (3+5j))




```python
len(t5) # lenght of the tuple
```




    4



### 2. Tuple Indexing


```python
print(t)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
```

    ()
    (1, 2, 3)
    (1.5, 2.5, 3.5, 4.5, 5.5)
    ('ravi', 'beri', 'cpl')
    (22, 35, 55, (65, 34, 57), (21, 98))
    (10, 2.5, 'ravi', (3+5j))
    


```python
t1=(10,20,30,40,50,60,70,80,90,100)
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
t1[0] # First index value
```




    10




```python
t1.count(10)
```




    1




```python
t1[-1] # Last element of the tuple
```




    100




```python
for i in enumerate(t1):
    print(i)
```

    (0, 10)
    (1, 20)
    (2, 30)
    (3, 40)
    (4, 50)
    (5, 60)
    (6, 70)
    (7, 80)
    (8, 90)
    (9, 100)
    (10, 'Raviteja')
    

### 3. Tuple Slicing


```python
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
t1[0:10] # prints all the elements from starting to 10th (i.e, n-1=9th) index element
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
t1[:3]
```




    (10, 20, 30)




```python
t1[3:]
```




    (40, 50, 60, 70, 80, 90, 100)




```python
t1[::-1]
```




    (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)




```python
t1[-2:]
```




    (90, 100)




```python
t1[:-2]
```




    (10, 20, 30, 40, 50, 60, 70, 80)




```python
t1[:]
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)



### 4. Remove & Change items


```python
t1[0]=1
t1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[41], line 1
    ----> 1 t1[0]=1
          2 t1
    

    TypeError: 'tuple' object does not support item assignment



```python
t2=t1*3
t2
```




    [1,
     20,
     1000,
     40,
     50,
     60,
     70,
     80,
     90,
     100,
     'Raviteja',
     1,
     20,
     1000,
     40,
     50,
     60,
     70,
     80,
     90,
     100,
     'Raviteja',
     1,
     20,
     1000,
     40,
     50,
     60,
     70,
     80,
     90,
     100,
     'Raviteja']




```python
del t1[0]
t1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[43], line 1
    ----> 1 del t1[0]
          2 t1
    

    TypeError: 'tuple' object doesn't support item deletion



```python
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
t1=(10,20,30,40,50,60,60,70,80,90,100)
t1
```




    (10, 20, 30, 40, 50, 60, 60, 70, 80, 90, 100)




```python
t1[2]=1000
t1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[13], line 1
    ----> 1 t1[2]=1000
          2 t1
    

    TypeError: 'tuple' object does not support item assignment


### 5. Loop through tuple


```python
l1=[10,20,30,40,50,60,70,80,90,100]
l1
```




    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]




```python
for i in enumerate(t1):
    print(i)
```

    (0, 10)
    (1, 20)
    (2, 30)
    (3, 40)
    (4, 50)
    (5, 60)
    (6, 70)
    (7, 80)
    (8, 90)
    (9, 100)
    


```python
for i in t1:
    print(i)
```

    10
    20
    30
    40
    50
    60
    70
    80
    90
    100
    

### 6. Tuple membership


```python
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
10 in t1
```




    True




```python
1000 in t1
```




    False




```python
if 10 in t1:
    print("It's perfect")
else:
    print("It's not perfect")
```

    It's perfect
    


```python
if 1000 in t1:
    print("It's perfect")
else:
    print("It's not perfect")
```

    It's not perfect
    

### 7. Indexing


```python
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
t1.index(10)
```




    0




```python
t1.index(100)
```




    9



### 8. Sorting


```python
t1
```




    (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)




```python
sorted(t1)
```




    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]




```python
sorted(t1, reverse=True)
```




    [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]



# Tuple is completed


```python

```
