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

### part 3
As your extended family has grown, members have gotten married and/or had children. Families usually get gifts for members of their immediate family, so it doesn’t make a lot of sense for anyone to be a Secret Santa for a member of their immediate family (spouse, parents, or children). Modify your program to take this constraint into consideration when choosing Secret Santas.

## Instructions

### Application usage

```python
python3 -m secret_santa
```

```unix
soyel@personal-pc:~/git/secret_santa$ python3 -m secret_santa
Step 1: Please enter the names of family members
            enter blank line to input immediate family mapping
santa
banta
alexa
siri
google

Step 2: Please enter members of immediate family separated by |
            enter blank line to generate the match
santa,banta

Matched pairs: {'alexa': 'siri', 'google': 'banta', 'banta': 'santa', 'santa': 'google', 'siri': 'alexa'}
Press Y key to simulate match for 2023
Y
Matched pairs: {'alexa': 'banta', 'google': 'santa', 'banta': 'siri', 'santa': 'alexa', 'siri': 'google'}
Press Y key to simulate match for 2024
Y
Matched pairs: {'alexa': 'santa', 'google': 'siri', 'banta': 'google', 'santa': 'banta'}
Press Y key to simulate match for 2025
Y
Matched pairs: {'alexa': 'google', 'google': 'banta', 'banta': 'santa', 'santa': 'siri', 'siri': 'alexa'}
Press Y key to simulate match for 2026
Y
Matched pairs: {'alexa': 'banta', 'google': 'santa', 'banta': 'siri', 'santa': 'google'}
Press Y key to simulate match for 2027
Y
Matched pairs: {'alexa': 'siri', 'google': 'alexa', 'banta': 'google', 'santa': 'banta', 'siri': 'santa'}
Press Y key to simulate match for 2028
N
```

### Testing
```python
python3 -m unittest
```

```unix
.....
----------------------------------------------------------------------
Ran 8 tests in 0.011s

OK
```



## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)