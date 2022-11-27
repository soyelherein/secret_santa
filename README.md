# Secret Santa challenge
Imagine that every year your extended family does a "Secret Santa" gift exchange.
For this gift exchange, each person draws another person at random
and then gets a gift for them.
This program that will choose a Secret Santa for everyone
given a list of all the members of your extended family.
Obviously, a person cannot be their own Secret Santa.
## Instructions

### Running appication

```python
python3 -m app
```

```unix
soyel@personal-pc:~/git/secret_santa$ python3 -m secret_santa
Please enter the names of family members
            enter blank line to generate the match
santa
banta
alexa

Matched pairs: {'banta': 'santa', 'alexa': 'banta', 'santa': 'alexa'}
```

### Testing
```python
python3 -m unittest
```

```unix
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```



## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)