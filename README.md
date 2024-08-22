## How to reproduce

Install project dependencies:
```
pipenv install
```

Then run the app:
```
textual run --dev darts.__main__:main
```
and select `Exit` from option list. It should produce a very succint error:
```
Traceback (most recent call last):
  File "<string>", line 12, in <module>
AttributeError: 'NoneType' object has no attribute 'run'
```
