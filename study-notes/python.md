## numpy
### numpy.choice
```python
numpy.random.choice(2, 500, p=[0.5, 0.5])
```
### numpy.roll
```python
x = np.arange(10)
np.roll(x, 2)
```
Result in `array([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])`

## pandas

### pandas: conditional change
```python
df.ix[df.A == True, 'A'] = 1
```
