# Data STructures- user will define the value more than one value
# 1.list
# 2.tuple
# 3.set
# 4.dict


```python
l=[]
l
```




    []




```python
len(l)
```




    0




```python
l.append(10)
```


```python
l
```




    [10]




```python
len(l)
```




    1




```python
l.append(20)
l.append(30)
l.append(40)
l.append(50)
```


```python
l
```




    [10, 20, 30, 40, 50]




```python
len(l)
```




    5




```python
id(l)
```




    2736704832832




```python
print(type(l))
```

    <class 'list'>
    


```python
import keyword
keyword.kwlist
```




    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'async',
     'await',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']




```python
l
```




    [10, 20, 30, 40, 50]




```python
l[:]
```




    [10, 20, 30, 40, 50]




```python
l[1]
```




    20




```python
l[-1]
```




    50




```python
l1=l.copy()
l1
```




    [10, 20, 30, 40, 50]




```python
l == l1
```




    True




```python
print(len(l))
print(len(l1))
```

    5
    5
    


```python
l1
```




    [10, 20, 30, 40, 50]




```python
l1.append(2.4)
l.append(True)
l1.append(2+3j)
```


```python
l1
```




    [10, 20, 30, 40, 50, 2.4, (2+3j)]




```python
l1.append(50)
```

# 


```python
l1
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50]




```python
l1.count(50)
```




    3




```python
l1.count(10)
```




    1




```python
l2=l1.copy()
l2
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50]




```python
l2.append(True)
```


```python
l2
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50, True]




```python
l2
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50]




```python
l2.append(True)
l2
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50, True]




```python
l3=l2.copy()
l3
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50, True]




```python
l3
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50, True]




```python
l3.(True)
l3
```


      Cell In[94], line 1
        l3.del(True)
           ^
    SyntaxError: invalid syntax
    



```python
l3
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50]




```python
del l2

```


```python
l2
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[100], line 1
    ----> 1 l2
    

    NameError: name 'l2' is not defined



```python
l3
```




    [10, 20, 30, 40, 50, 2.4, (2+3j), 50, 50]




```python
l3.clear()
```


```python
l3
```




    []




```python

```


```python

```


```python

```


```python

```
