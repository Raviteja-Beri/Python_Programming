# Python- Complex Data type


```python
n1=3+5j
print(n1.real)
print(n1.imag)
```

    3.0
    5.0
    


```python
a=5+7j
b=4+3j
```


```python
print(a+b)
```

    (9+10j)
    


```python
print(a*b)
```

    (-1+43j)
    


```python
print(a-b)
```

    (1+4j)
    


```python
print(a/b)
```

    (1.64+0.52j)
    


```python
print(abs(a))
```

    8.602325267042627
    


```python
print(abs(b))
```

    5.0
    


```python
z=3+4j
print(z.conjugate()) # writtens conjugate of the particular function
```

    (3-4j)
    


```python
# Complex Number in cmath Module
```


```python
import cmath
```


```python
z=1+1j
print(cmath.phase(z)) # It gives the phase (angle) of the complex numbers
```

    0.7853981633974483
    


```python
print(cmath.polar(z)) # It gives the polar form of a complex number i.e., magnitude and angle
```

    (1.4142135623730951, 0.7853981633974483)
    


```python
print(cmath.sqrt(z)) # It gives the square root of a complex number
```

    (1.09868411346781+0.45508986056222733j)
    


```python
n2=5+12j
print(cmath.sqrt(n2))
```

    (3+2j)
    


```python

```


```python

```


```python

```
