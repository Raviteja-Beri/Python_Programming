# Set


```python
s={}
s
```




    {}




```python
type(s)
```




    dict




```python
s1=set()
type(s1)
```




    set




```python
s1
```




    set()




```python
s2={10,15,5,20,30,40} # It gives you in order when the similar data is given
s2                    # Integers
```




    {5, 10, 15, 20, 30, 40}




```python
s3={'c','f','a','e','g'} # It is the same data type i.e, string
s3
```




    {'a', 'c', 'e', 'f', 'g'}




```python
s4={1,2,'ravi',1+3j,[1,2,3],(4,5,6),True} # Mixed data types
s4
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[16], line 1
    ----> 1 s4={1,2,'ravi',1+3j,[1,2,3],(4,5,6),True}
          2 s4
    

    TypeError: unhashable type: 'list'



```python
s5={2,3.4,'nit',1+3j,False} # In mixed data types it wont give you in order
s5
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
print(s1)
print(s2)
print(s3)
print(s5)
```

    set()
    {20, 5, 40, 10, 30, 15}
    {'e', 'f', 'a', 'g', 'c'}
    {False, 2, 3.4, 'nit', (1+3j)}
    


```python
s2.add(30) # It will add in orderwise
```


```python
s2
```




    {5, 10, 15, 20, 30, 40}




```python
s2.add(35)
s2
```




    {5, 10, 15, 20, 30, 35, 40}




```python
s2.add(100)
s2
```




    {5, 10, 15, 20, 30, 35, 40, 100}




```python
s2[:] # Set index slicing is not allowed. Only List and Tuple allows index slicing.
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[32], line 1
    ----> 1 s2[:]
    

    TypeError: 'set' object is not subscriptable



```python
s2[1:5] # Set index slicing is not allowed. Only List and Tuple allows index slicing.
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[34], line 1
    ----> 1 s2[1:5]
    

    TypeError: 'set' object is not subscriptable



```python
s2
```




    {5, 10, 15, 20, 30, 35, 40, 100}




```python
s5
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
s4=s5.copy() # Copy function is allowed
s4
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
s4.add(2) # In Duplicate elements are not allowed. In List and Tuple it is allowed.
s4
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
s5
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
s5.clear() # it removes all the elements.
s5         # Shift + Tab = Docstring
           # Doctsring = Help of the functions
```




    set()




```python
s5
```




    set()




```python
del s5
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[56], line 1
    ----> 1 del s5
    

    NameError: name 's5' is not defined



```python
s4
```




    {(1+3j), 2, 3.4, False, 'nit'}




```python
s4.remove((1+3j)) # To Remove an element from a set; it must be a member
```


```python
s4
```




    {2, 3.4, False, 'nit'}




```python
s3
```




    {'a', 'c', 'e', 'f', 'g'}




```python
s3.discard('m') # 'm' is not a member of the list but it wont throw you any error unlike remove() function.
s3
```




    {'a', 'c', 'e', 'f', 'g'}




```python
s3.remove('m') # Its not as discard so it throws you an error.
s3
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Cell In[68], line 1
    ----> 1 s3.remove('m')
          2 s3
    

    KeyError: 'm'



```python
s3.discard('f') # it deletes the element from the list.
s3
```




    {'a', 'c', 'e', 'g'}




```python
s3
```




    {'a', 'c', 'e', 'g'}




```python
s3.pop() # Pop=index level output. By default it wont give yo the last element.
        # It gives a random index value.
```




    'e'




```python
s2
```




    {5, 10, 15, 20, 30, 35, 40, 100}




```python
s2.pop(4) # In set Indexing is not allowed. so it throws an error.
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[78], line 1
    ----> 1 s2.pop(4)
    

    TypeError: set.pop() takes no arguments (1 given)



```python
s2.pop()
```




    35




```python
s2
```




    {5, 10, 15, 20, 30, 40, 100}




```python
for i in enumerate(s2): # Loops also works in set.
    print(i)
```

    (0, 20)
    (1, 5)
    (2, 100)
    (3, 40)
    (4, 10)
    (5, 30)
    (6, 15)
    


```python
for i in s2:
    print(i)
```

    20
    5
    100
    40
    10
    30
    15
    


```python
s2
```




    {5, 10, 15, 20, 30, 40, 100}




```python
2 in s2 # set membership
```




    False




```python
10 in s2
```




    True




```python
s2
```




    {5, 10, 15, 20, 30, 40, 100}




```python
s3
```




    {'a', 'c', 'g'}




```python
s2.update(s3)
s2
```




    {10, 100, 15, 20, 30, 40, 5, 'a', 'c', 'g'}



# Set Operations (very important)
### 1. Union
### 2. Disjoint
### 3. Difference
### 4. Symmetric_Difference

#### 1. Union


```python
s6={1,2,3,4,5}
s7={4,5,6,7,8}
s8={8,9,10}

```


```python
s6.union(s7) # Return the union of sets as a new set.It filters the duplicate elements.
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
s6.union(s7,s8)
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}




```python
s6 | s7 # |=pipe sign. union function can aloso written as pipe symbol
```




    {1, 2, 3, 4, 5, 6, 7, 8}




```python
s6 | s7 | s8
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}




```python
print(s6)
print(s7)
print(s8)
```

    {1, 2, 3, 4, 5}
    {4, 5, 6, 7, 8}
    {8, 9, 10}
    


```python
s6.intersection(s7) # Common elements are given as output
```




    {4, 5}




```python
s6.intersection(s8) # No common elelments. so empty set
```




    set()




```python
s7.intersection(s8)
```




    {8}




```python
s6 & s7 # '&' = Intersection symbol
```




    {4, 5}




```python
print(s6)
print(s7)
print(s8)
```

    {1, 2, 3, 4, 5}
    {4, 5, 6, 7, 8}
    {8, 9, 10}
    


```python
s6.difference(s7)
```




    {1, 2, 3}




```python
s7.difference(s8)
```




    {4, 5, 6, 7}




```python
s6 - s7 # '-' = difference symbol
```




    {1, 2, 3}




```python
s7 - s8
```




    {4, 5, 6, 7}




```python
s8 - s7
```




    {9, 10}




```python
print(s6)
print(s7)
print(s8)
```

    {1, 2, 3, 4, 5}
    {4, 5, 6, 7, 8}
    {8, 9, 10}
    


```python
s6.symmetric_difference(s7) # Return the symmetric difference of two sets as a new set.It removes common elements.
```




    {1, 2, 3, 6, 7, 8}




```python

```


```python

```


```python

```


```python

```


```python

```
