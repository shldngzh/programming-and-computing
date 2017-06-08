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


## logging
```python
import logging


logger = logging.getLogger()
h = logging.FileHandler(filename=[FILEPATH], mode='w')
logger.addHandler(h)
logger.setLevel(logging.INFO)
logging.info("Some Info")
logger.log(logging.INFO, msg='Some MEssage')
h.close()
logger.removeHandler(h)
```
