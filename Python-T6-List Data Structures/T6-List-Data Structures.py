# List Data Structures


```python
l=[10,20,34,56,3,15,28]
l
```




    [10, 20, 34, 56, 3, 15, 28]




```python
l.insert(2,33)
l
```




    [10, 20, 33, 34, 56, 3, 15, 28]




```python
l.pop(6)
```




    15




```python
l
```




    [10, 20, 33, 34, 56, 3]




```python
l.pop(5)
```




    3




```python
l
```




    [10, 20, 33, 34, 56]




```python
l.append(99)
l
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l.copy()
l
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l1=l.copy()
l1
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l.copy(l1)
l
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[21], line 1
    ----> 1 l.copy(l1)
          2 l
    

    NameError: name 'l1' is not defined



```python
l1
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
print(l1 != l1)
```

    False
    


```python
print(l)
print(l1)
```

    [10, 20, 34, 56, 3, 15, 28, 99]
    [10, 20, 34, 56, 3, 15, 28, 99]
    


```python
l.clear()
```


```python
l
```




    []




```python
l1
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
l2=l1.copy()
```


```python
l2
```




    [10, 20, 34, 56, 3, 15, 28, 99]




```python
print(l1)
print(l2)
```

    [10, 20, 34, 56, 3, 15, 28, 99]
    [10, 20, 34, 56, 3, 15, 28, 99]
    


```python
l1.append(20)
l2.append(20)
print(l1)
print(l2)
```

    [10, 20, 34, 56, 3, 15, 28, 99, 20]
    [10, 20, 34, 56, 3, 15, 28, 99, 20]
    


```python
l1.append(56)
l2.append(56)
print(l1)
print(l2)
```

    [10, 20, 34, 56, 3, 15, 28, 99, 20, 56]
    [10, 20, 34, 56, 3, 15, 28, 99, 20, 56]
    


```python
l1.count(20)
l2.count(56)
```




    2




```python
l1.extend(l2)
l1
```




    [10, 20, 34, 56, 3, 15, 28, 99, 20, 56, 10, 20, 34, 56, 3, 15, 28, 99, 20, 56]




```python
l1
```




    [10, 20, 34, 56, 3, 15, 28, 99, 20, 56, 10, 20, 34, 56, 3, 15, 28, 99, 20, 56]




```python
l1.index(56)
```




    3




```python
l1.insert(3,46)
```


```python
l1
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[1], line 1
    ----> 1 l1
    

    NameError: name 'l1' is not defined



```python
l1.pop(20)
l1
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[3], line 1
    ----> 1 l1.pop(20)
          2 l1
    

    NameError: name 'l1' is not defined



```python
l1
```




    [10,
     20,
     34,
     46,
     46,
     56,
     3,
     15,
     28,
     99,
     20,
     56,
     10,
     20,
     34,
     56,
     3,
     15,
     28,
     99,
     56]




```python
l1.remove(46)
l1
```




    [10, 20, 34, 46, 56, 3, 15, 28, 99, 20, 56, 10, 20, 34, 56, 3, 15, 28, 99, 56]




```python
l1.sort()
l1
```




    [3, 3, 10, 10, 15, 15, 20, 20, 20, 28, 28, 34, 34, 46, 56, 56, 56, 56, 99, 99]




```python
l1.sort(reverse=True)
l1
```




    [99, 99, 56, 56, 56, 56, 46, 34, 34, 28, 28, 20, 20, 20, 15, 15, 10, 10, 3, 3]




```python
l1
```




    [99, 99, 56, 56, 56, 56, 46, 34, 34, 28, 28, 20, 20, 20, 15, 15, 10, 10, 3, 3]




```python
l1
```




    [99, 99, 56, 56, 56, 56, 46, 34, 34, 28, 28, 20, 20, 20, 15, 15, 10, 10, 3, 3]




```python
all(l1)  # Will Return false if any one value is '0'. that is it considers '0' as a false value. 
```




    True




```python
l1.append(0)
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     0]




```python
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     0]




```python
all(l1) # Will Return false if any one value is '0'. that is it considers '0' as a false value.
```




    False




```python
any(l1) # gives you the value if any one of the element is '0'
```




    True




```python
l1.append('True')
```


```python
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     0,
     'True']




```python
l.append('False')
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     0,
     'True']




```python
l1.append('False')
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     0,
     'True',
     'False']




```python
all(l1) # cause we have 'False' and '0' in the list. So it gives as false
```




    False




```python
any(l1)
```




    True




```python
l1.remove(0)
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     'True',
     'False']




```python
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     'True',
     'False']




```python
l1.remove('False')
l1
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     'True']




```python
l1 # It has all true values. now you will get the perfect output.
```




    [99,
     99,
     56,
     56,
     56,
     56,
     46,
     34,
     34,
     28,
     28,
     20,
     20,
     20,
     15,
     15,
     10,
     10,
     3,
     3,
     'True']




```python
all(l1)
```




    True




```python
any(l1)
```




    True




```python
l1=[99, 99, 56, 56, 56, 56, 46, 34, 34, 28, 28, 20, 20, 20, 15, 15, 10, 10, 3, 3]
l1.sort()
l1
```




    [3, 3, 10, 10, 15, 15, 20, 20, 20, 28, 28, 34, 34, 46, 56, 56, 56, 56, 99, 99]




```python
l1.append('Raviteja')
l1
```




    [3,
     3,
     10,
     10,
     15,
     15,
     20,
     20,
     20,
     28,
     28,
     34,
     34,
     46,
     56,
     56,
     56,
     56,
     99,
     99,
     'Raviteja']




```python
l1[-1]='nit'
l1
```




    [3,
     3,
     10,
     10,
     15,
     15,
     20,
     20,
     20,
     28,
     28,
     34,
     34,
     46,
     56,
     56,
     56,
     56,
     99,
     99,
     'nit']




```python
l1[-1][0] # [-1]= last index value i.e., backward slicing
          # [0]= It gives you the first index value of that particular list
          # It is called as nested slicing
```




    'n'




```python
l1[-1][1] # [-1]= last index value
          # [1]= second index value of the 'nit'
```




    'i'




```python
print(l1[-1][0])
print(l1[-1][1])
print(l1[-1][2])
```

    n
    i
    t
    


```python
l1
```




    [3,
     3,
     10,
     10,
     15,
     15,
     20,
     20,
     20,
     28,
     28,
     34,
     34,
     46,
     56,
     56,
     56,
     56,
     99,
     99,
     'nit']




```python
l1.remove('nit')
l1
```




    [3, 3, 10, 10, 15, 15, 20, 20, 20, 28, 28, 34, 34, 46, 56, 56, 56, 56, 99, 99]




```python
l1[0:11:2] # 0: This is the starting index. The slice will begin at the element with index 0 (the first element).
           # 11: This is the stopping index. The slice will go up to, but not include, the element with index 11.
           # 2: This is the step. It determines how many elements to skip between each selected element.
```




    [3, 10, 15, 20, 20, 28]




```python
l1[0:15:3]
```




    [3, 10, 20, 28, 34]




```python
l1=[1,2,3,5,7,10,15,20,19,18]
l1[0:5:1]
```




    [1, 2, 3, 5, 7]




```python
l1[0:8:2]
```




    [1, 3, 7, 15]




```python
l1
```




    [1, 2, 3, 5, 7, 10, 15, 20, 19, 18]




```python
for i in enumerate(l1):
    print(i)
```

    (0, 1)
    (1, 2)
    (2, 3)
    (3, 5)
    (4, 7)
    (5, 10)
    (6, 15)
    (7, 20)
    (8, 19)
    (9, 18)
    


```python
l1=[10,20,30,40,50]
20 in l1
```




    True




```python
60 in l1
```




    False



# List Data Structures Completed


```python

```
