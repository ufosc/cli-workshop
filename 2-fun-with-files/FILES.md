# 2 - Fun with Files

Lets learn how to:

- View a file
- View the top of a file
- View the bottom of a file
- Find a file
- Search a file
- Split a file

## View a file

To view the total contents of a file we can use the `cat` command, or `concatenate`

```bash
    $ cat imshort
im short
```

## View the top of a file

To view the top 10 lines of a file we use the `head` command. As you can imagine your head is on top of your body.

```bash
    $ head test.txt
Dakota|Jon|Fred|Fred|Andrew|Logan|Fred|Isabella|Jon|Alice
Isabella|Alice|Hunter|Hunter|Andrew|Anna|Hunter|Logan|Jess|Andrew
Alice|Alice|Bob|Logan|Fred|Logan|Jess|Hunter|Bob|Jon
Jess|Anna|Jon|Bob|Logan|Jon|Anna|Anna|Jess|Andrew
Andrew|Fred|Hunter|Hunter|Bob|Alice|Alice|Jon|Jess|Andrew
Fred|Anna|Jess|Logan|Jon|Fred|Anna|Anna|Isabella|Jon
Hunter|Andrew|Hunter|Dakota|Jon|Jess|Andrew|Jon|Bob|Dakota
Logan|Fred|Hunter|Fred|Andrew|Andrew|Isabella|Dakota|Jon|Dakota
Andrew|Jon|Andrew|Isabella|Logan|Isabella|Andrew|Bob|Dakota|Hunter
Hunter|Alice|Bob|Dakota|Logan|Andrew|Bob|Fred|Jon|Logan
```

You can change the number of files you want to see with the -n flag.

```bash
    $ head -n1 test.txt
Dakota|Jon|Fred|Fred|Andrew|Logan|Fred|Isabella|Jon|Alice
```

## View the bottom of a file

To view the top 10 lines of a file we use the `tail` command. As you can imagine if you had a tail your tail would be on bottom of your body.

```bash
    $ head test.txt
Alice|Hunter|Isabella|Andrew|Jon|Alice|Logan|Logan|Dakota|Anna
Fred|Andrew|Anna|Bob|Alice|Alice|Logan|Jon|Isabella|Hunter
Hunter|Anna|Anna|Logan|Alice|Andrew|Anna|Dakota|Dakota|Jess
Jess|Bob|Bob|Jon|Dakota|Jess|Dakota|Bob|Jon|Isabella
Andrew|Andrew|Bob|Hunter|Bob|Jess|Hunter|Isabella|Logan|Fred
Anna|Hunter|Jon|Anna|Jon|Hunter|Isabella|Anna|Jon|Dakota
Jess|Alice|Dakota|Andrew|Jon|Bob|Fred|Andrew|Jess|Jon
Alice|Anna|Isabella|Alice|Hunter|Bob|Fred|Alice|Dakota|Bob
Anna|Bob|Bob|Jon|Logan|Logan|Jess|Dakota|Dakota|Jon
Andrew|Dakota|Alice|Logan|Alice|Jess|Andrew|Logan|Dakota|Isabella
```

You can change the number of files you want to see with the -n flag.

```bash
    $ head -n1 test.txt
Andrew|Dakota|Alice|Logan|Alice|Jess|Andrew|Logan|Dakota|Isabella
```

## Find a file

Now say youre searching for all text files in some directory. You can use the `find` command to locate these and even run commands on them.

**NOTE:** Unlike most commands the directory comes **BEFORE** the flags.

Locate all text files

```bash
    $ find . -name "*.txt"
./1-navigating/test2/test.txt
./2-fun-with-files/test.txt
```

What happens if you put the directory after the experssion:

```bash
    $ find -name "*.txt" .
find: illegal option -- n
usage: find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
    find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
```

## Search a file

Now we can do fast advanced file searches using the `grep` program. This comes from "Globally search for a Regular Expression and Print matching lines".

As you can see from the name this tool can do advanced searches using Regular Expressions. Now this tutorial will not go into forming regular expressions but you can [see this link](https://regexr.com/) for more information.

Lets search for the word short in the imshort file.

```bash
    $ grep "short" imshort
im short
```

Wow it printing the matching line. Now this was a little underwhelming as it only had one file.

Now lets search for the phrase "find me" hidden in the test.txt.

```bash
    $ grep "find me" test.txt
```

Huh theres nothing being returned. This is probably because grep searches CASE-SENSITIVELY.

Lets search case insensitively.

```bash
    $ grep --ignore-case "find me" test.txt 
FIND ME
```

Cool so we found it and we now know its in the file but what if we wanted to know which line number its on?

We can use the -n flag to find out.

```bash
    $ grep --ignore-case -n "find me" test.txt 
913:FIND ME
```

Grep also has a lot of cool features and flags so please look at the manual with `man grep` or search online for `grep manual`.

## Spliting files

Now we know that the test.txt file has a bunch of columns sperated by the pipe `|`. What if we wanted to just get the first column of the file?

We can use the `cut` command. This allows you to split a line by byte, character, or deliminator.

We are going to get the first column and split by deliminator so we will use the -d flag.

```bash
    $ cut -f 1 -d '|' test.txt
...large amount of text...
```
