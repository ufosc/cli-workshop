# Piping and Combining the Previous Steps

## Redirecting output

Lets redirect output from standard out and standard error. Bash/ZSH/most shells will let you redirect the output to different filedescriptors to different commands or even files.

Lets first just run generate.py

```bash
    $ python3 generate.py 
Jess|Jess|Alice|Bob|Andrew|Alice|Jess|Alice|Jess|Hunter
This is an error
...
```

As you'll see the program interlaces standard output and standard error.

Lets pipe just standard error to a file

```bash
    $ python3 generate.py 2>errors.txt
Dakota|Alice|Andrew|Jon|Anna|Alice|Bob|Jess|Jess|Anna
Isabella|Bob|Bob|Hunter|Alice|Anna|Anna|Dakota|Dakota|Alice
Jess|Anna|Isabella|Bob|Bob|Anna|Alice|Fred|Bob|Dakota
Fred|Anna|Fred|Andrew|Fred|Andrew|Dakota|Hunter|Jon|Jon
Logan|Andrew|Jess|Alice|Jon|Jon|Logan|Logan|Hunter|Jon
Jess|Jon|Fred|Bob|Dakota|Isabella|Bob|Hunter|Andrew|Bob
```

See no more standard error.

```bash
    $ cat errors.txt
This is an error
This is an error
This is an error
This is an error
...
```

Now lets output just standard output. 
```bash
    $ python3 generate.py 1>names.txt 2>errors.txt
This is an error
This is an error
This is an error
This is an error
...
```

Now lets output both! Notice I dropped the 1. Thats because it is the default.

```bash
$ python3 generate.py 1>names.txt 2>errors.txt
```

## Piping!

Now lets pipe between commands. This allows you to take the output of one command and move it to another.

Lets pipe the output of the program to `grep` to see if hunter is listed three times in a row

```bash
    $ python3 generate.py 2>/dev/null | grep "Hunter|Hunter|Hunter" > HunterHunterHunter.txt
    $ cat HunterHunterHunter.txt
Andrew|Hunter|Hunter|Hunter|Jon|Anna|Logan|Isabella|Bob|Hunter
Dakota|Jon|Logan|Dakota|Logan|Dakota|Hunter|Hunter|Hunter|Anna
Jon|Hunter|Hunter|Hunter|Fred|Dakota|Hunter|Andrew|Fred|Dakota
Jon|Bob|Andrew|Hunter|Hunter|Hunter|Andrew|Isabella|Bob|Andrew
Anna|Hunter|Hunter|Hunter|Hunter|Logan|Logan|Anna|Bob|Fred
Anna|Bob|Andrew|Hunter|Hunter|Hunter|Andrew|Bob|Fred|Fred
...
```

## Challenges

1. Can you create a file where just the first column contains "Anna"?
2. Using the wc -l command to find the count of lines how many lines have "Logan|Logan|Logan"? (You'll need to pipe twice or lookup a grep flag)

## Advanced Challenge

1. Whats the distribution (AKA the count of each name) in the 3rd column? (You'll need cut and sort with flags)
2. Whats the count of Bob in the 3rd column? (You'll need grep, wc -l, cut)
