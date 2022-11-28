# Secret Santa challenge
### part 1
Imagine that every year your extended family does a "Secret Santa" gift exchange.
For this gift exchange, each person draws another person at random
and then gets a gift for them.
This program that will choose a Secret Santa for everyone
given a list of all the members of your extended family.
Obviously, a person cannot be their own Secret Santa.

### part 2
After the third year of having the Secret Santa gift exchange, you’ve heard complaints of having the same Secret Santa year after year. Modify your program so that a family member can only have the same Secret Santa once every 3 years.

## Instructions

### Running appication

```python
python3 -m secret_santa
```

```unix
soyel@personal-pc:~/git/secret_santa$ python3 -m secret_santa
Please enter the names of family members
            enter blank line to generate the match
santa
banta
alexa
siri

Matched pairs: {'banta': 'alexa', 'alexa': 'santa', 'santa': 'siri', 'siri': 'banta'}
Press Y key to simulate match for 2023
y
Matched pairs: {'banta': 'siri', 'alexa': 'banta', 'santa': 'alexa', 'siri': 'santa'}
Press Y key to simulate match for 2024
y
Matched pairs: {'banta': 'santa', 'alexa': 'siri', 'santa': 'banta', 'siri': 'alexa'}
Press Y key to simulate match for 2025
y
Matched pairs: {'banta': 'alexa', 'alexa': 'santa', 'santa': 'siri', 'siri': 'banta'}
Press Y key to simulate match for 2026
N
```

### Testing
```python
python3 -m unittest
```

```unix
.....
----------------------------------------------------------------------
Ran 7 tests in 0.007s

OK
```



## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)