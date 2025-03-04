```python
l=[10,20,34,56,3,15,28]
l
```




    [10, 20, 34, 56, 3, 15, 28]




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
     20,
     56]




```python
l1.pop(20)
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

```
