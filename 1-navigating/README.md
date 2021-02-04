# 1 - Navigating the Terminal & Files

Brief introduction to:

- Moving between directories
- Creating new directories
- Creating new files
- Moving/copying directories/files

## How do I even know where I am?

What if I walk away and I don't remember what path I'm in?

One way is to use `PWD - Print Working Directory`.

```bash
    $ pwd
/Users/hunterjarrell/Projects/cli-tutorial
```

## Move between directories

We can change our current directory with the `cd` command, or `change directory`.

```bash
    $ cd 1-navigating
```

And move back up using the shortcut `..`

```bash
    $ cd ..
```

## How do I know what files are around me?

Lets use the `ls` command which is short for `list`. 

```bash
    $ ls
1-navigating README.md ...
```

As you can see this just has multiple columns with both the files and directories in your current directory. 

### Get more information from `ls`

We can get way more information with the ls command!

Say we want to see the size of the files or maybe the permissions.

We can use different flags to view different things. 

List more information:

```bash
    $ ls -l
total 8
drwxr-xr-x  3 hunterjarrell  staff   96 Feb  4 15:25 1-navigating
-rw-r--r--  1 hunterjarrell  staff  790 Feb  4 15:20 README.md
```

Hidden files:

```bash
    $ ls -a
.            ..           1-navigating README.md
```

Combined:

```bash
    $ ls -la
total 8
drwxr-xr-x   4 hunterjarrell  staff   128 Feb  4 15:22 .
drwxr-xr-x  47 hunterjarrell  staff  1504 Feb  4 15:19 ..
drwxr-xr-x   3 hunterjarrell  staff    96 Feb  4 15:25 1-navigating
-rw-r--r--   1 hunterjarrell  staff   790 Feb  4 15:20 README.md
```

## Lets create a new directory

Now I want to create a directory named test. This is very easy to do using `mkdir` or `make directory`.

First lets ensure we are in 1-navigating.

```bash
    $ pwd
/Users/hunterjarrell/Projects/cli-tutorial
    $ cd 1-navigating
```

Now lets create our test directory.

```bash
    $ mkdir test
```

Now lets move into it.

```bash
    $ cd test
```

## Create a new file

Now we can create an empty file using the `touch` command.

Now this tool can be used for some more advanced features but for now we are going to use it to create a new file.

```bash
    $ touch test.txt
```

## Copy this file

Okay to copy a file we can use the `cp` command or `copy`.

```bash
    $ cp test.txt test2.txt
```

## Move/rename a file

Renaming and moving files are the same command, `mv` or `move`.

```bash
    $ mv test2.txt test3.txt
```

Watch out as this will overwrite same named files

```bash
    $ mv test3.txt test.txt
    $ ls
test.txt
```

## Copy & Move directories

To copy a directory you'll need to pass the -r flag, which stands for recursive.

Lets move up a directory and copy the test directory.

```bash
    $ cd ..
    $ cp -r test test2
```

Now lets move it

```bash
    $ mv test2 test3
```
