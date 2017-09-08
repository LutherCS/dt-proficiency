
# Software Development Tools

This notebook describes basic commands we cover in class. You should execute them in the terminal of your Ubuntu.

* [Basic Linux Commands](http://www.debianhelp.co.uk/commands.htm)
* [Basic UNIX commands](http://mally.stanford.edu/~sr/computing/basic-unix.html)
* [UNIX command summary](http://www.bsd.org/unixcmds.html)
* [Unix Commands](https://pangea.stanford.edu/computing/unix/shell/commands.php)
* [Introduction to Unix commands](https://kb.iu.edu/d/afsk)
* [50 Most Frequently Used UNIX / Linux Commands (With Examples)](http://www.thegeekstuff.com/2010/11/50-linux-commands/)


## Linux commands

### General

* alias
* clear
* echo
* exit
* history
* less
* logout (use Ctrl+D)
* **man**

### Files and directories

* cat
* cd
* chmod
* chown (requires **sudo**)
* cp
* find
* ls
* locate
* mkdir
* mv
* pwd
* rm
* rmdir
* tail
* touch

### User management

* adduser (requires **sudo**)
* deluser (requires **sudo**)
* groups
* passwd
* usermod (requires **sudo**)
* w
* who
* whoami

### System

* date
* shutdown
* uname
* uptime
* which

### Process management

* kill
* ps
* top

### Networking

* ifconfig
* ip
* nslookup
* ping

### Tools

* bc
* comm
* cut
* sort
* tr
* uniq
* wc

### Pipes and redirection
* Pipe: |
* Input redirection: <
* Output redirection: >
* Standard output stream 1>
* Standard error stream 2>


```bash
%%bash
# This is a comment
# Print something to the standart output
echo 'Hello world'
# Get help
man
# Proper usage: man command
```

    Hello world


    What manual page do you want?



```bash
%%bash
# Find a file by name in a specific directory
find /usr -name american-english
```

    /usr/share/dict/american-english



```bash
%%bash
# Find a file, another command
locate american-english
```

    /usr/share/dict/american-english
    /usr/share/man/man5/american-english.5.gz



```bash
%%bash
# Print the name of the current (working) directory
pwd
```

    /home/faculty/yasiro01/courses/swdt-class-pub



```bash
%%bash
# Navigate between directories
pwd
# Go to the root directory
cd /
pwd
# Go to *your* home directory
cd
pwd
# Go to the a specific subdirectory of the current one
cd courses/swt-class-pub
pwd
# Go to *your* home directory
cd ~
pwd
# Go to the parent directory (up one level)
cd ..
pwd
```

    /home/faculty/yasiro01/courses/swdt-class-pub
    /
    /home/faculty/yasiro01
    /home/faculty/yasiro01
    /home/faculty/yasiro01
    /home/faculty


    bash: line 10: cd: courses/swt-class-pub: No such file or directory



```bash
%%bash
# List the content (files and directories) of the current directory
ls
```

    fnord.txt
    library_gen.ipynb
    library.txt
    linux_commands.ipynb
    linux_commands.md
    passwd_gen.ipynb
    roster.txt
    sorted_words



```bash
%%bash
# List the content of the root directory
ls /
```

    bin
    boot
    dev
    etc
    home
    initrd.img
    initrd.img.old
    lib
    lib64
    lost+found
    media
    mnt
    nsr
    opt
    proc
    project
    restore
    root
    run
    sbin
    snap
    srv
    sys
    tmp
    usr
    var
    vmlinuz
    vmlinuz.old



```bash
%%bash
# List the content of the directory /home/faculty/yasiro01 in a long format
ls -l /home/faculty/yasiro01
```

    total 276
    drwxr-xr-x 6 yasiro01 Faculty   4096 Sep  8 12:34 courses
    -rw-r--r-- 1 yasiro01 users     8980 Sep 29  2016 examples.desktop
    drwxr-xr-x 3 yasiro01 users     4096 Feb 16  2017 public_html
    -rw-r--r-- 1 yasiro01 Faculty   7509 Sep  8 10:29 snippets.ipynb
    -rw-r--r-- 1 yasiro01 Faculty 215017 Oct 26  2016 SortCompare.ipynb
    -rw-r--r-- 1 yasiro01 Faculty  23124 Feb 16  2017 tao_of_python.ipynb
    -rw-r--r-- 1 yasiro01 Faculty   8520 Nov  3  2016 TreePlotting.ipynb



```bash
%%bash
# Display information about a specific file
ls -l linux_commands.ipynb
```

    -rw-r--r-- 1 yasiro01 Faculty 19671 Sep  8 13:02 linux_commands.ipynb



```bash
%%bash
# Display information about a non-existing file
ls -l new_file
```

    ls: cannot access 'new_file': No such file or directory



```bash
%%bash
# Create a new empty file
touch new_file
ls -l new_file
```

    -rw-r--r-- 1 yasiro01 Faculty 0 Sep  8 13:02 new_file



```bash
%%bash
# Write hello world to a file
echo hello world > example.txt
# Append current date (result of the date command) to a file at the second line
echo today is `date` >> example.txt
# Display file content
cat example.txt
# Display number of lines in a file
cat example.txt | wc
```

    hello world
    today is Fri Sep 8 13:02:35 CDT 2017
          2      10      49



```bash
%%bash
# Copy a file
cp example.txt another_example.txt
# * means any character(s). This command lists all files ending in example.txt
ls -l *example.txt
```

    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 another_example.txt
    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt



```bash
%%bash
# Move (or rename) a file
mv another_example.txt yet_another_example.txt
ls -l *example.txt
```

    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt
    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 yet_another_example.txt



```bash
%%bash
# Delete a file
rm yet_another_example.txt
ls -l *example.txt
```

    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt



```bash
%%bash
# Change a file mode
chmod 755 example.txt
ls -l *example.txt
chmod -w example.txt
ls -l *example.txt
# Numeric representation of the mode
chmod 644 example.txt
ls -l *example.txt
```

    -rwxr-xr-x 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt
    -r-xr-xr-x 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt
    -rw-r--r-- 1 yasiro01 Faculty 49 Sep  8 13:02 example.txt



```bash
%%bash
# Create (make) a new directory
mkdir new_dir
touch new_dir/new_file
ls new_dir
```

    new_file



```bash
%%bash
# Delete (remove) a directory
rm -rf new_dir
```


```bash
%%bash
# See your username
whoami
```

    yasiro01



```bash
%%bash
# Display groups the user belongs to
groups yasiro01
```

    yasiro01 : Faculty



```bash
%%bash
# See logged in users
who
```

    millbr02 pts/8        2017-09-05 14:18 (10.24.10.4)
    millbr02 pts/12       2017-08-30 09:21 (10.24.10.4)
    millbr02 pts/13       2017-08-30 09:44 (10.24.10.4)
    millbr02 pts/14       2017-09-06 09:13 (10.24.10.4)
    stuckmch pts/18       2017-09-06 15:18 (10.22.2.28)



```bash
%%bash
# See logged in users and their activity
w
```

     13:02:36 up 15 days,  5:54,  5 users,  load average: 1.15, 1.11, 1.04
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
    millbr02 pts/8    10.24.10.4       Tue14    3:39m  0.42s  0.36s ssh apc
    millbr02 pts/12   10.24.10.4       30Aug17  3days  6:13   3.00s -bash
    millbr02 pts/13   10.24.10.4       30Aug17  3days  0.27s  0.21s ssh apc
    millbr02 pts/14   10.24.10.4       Wed09   26:43m  0.25s  0.08s /usr/lib/postgresql/9.3/bin/psql world
    stuckmch pts/18   10.22.2.28       Wed15   45:34m  0.29s  0.06s sshd: stuckmch [priv]



```bash
%%bash
# Print the name of the system
uname -a
```

    Linux knuth 4.4.0-92-generic #115-Ubuntu SMP Thu Aug 10 09:04:33 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux



```bash
%%bash
# Print the date and time of the system
date
```

    Fri Sep  8 13:02:36 CDT 2017



```bash
%%bash
# Print the system's uptime
uptime
```

     13:02:36 up 15 days,  5:54,  5 users,  load average: 1.15, 1.11, 1.04



```bash
%%bash
# Print the path to the application by its name
which python
```

    /usr/bin/python



```bash
%%bash
# Display the result of a command execution
whoami
# Display the result of a command execution. Wrong way
echo whoami
# Ticks allow you to use the result of a command execution
echo `whoami`
# Ticks allow you to use the result of a command execution
`echo whoami`
```

    yasiro01
    whoami
    yasiro01
    yasiro01



```bash
%%bash
# Simple bash calculator
echo 2*2 | bc
echo 2^3 | bc
echo 160 / 10 | bc
```

    4
    8
    16



```bash
%%bash
# Pipes and calculations
ls -l
echo '---'
echo `ls -l`
echo '---'
echo `ls -l | wc -l`
echo '---'
echo `ls -l | wc -l` - 1
echo '---'
echo `ls -l | wc -l` - 1 | bc
```

    total 984
    -rw-r--r-- 1 yasiro01 Faculty     49 Sep  8 13:02 example.txt
    -rw-r--r-- 1 yasiro01 Faculty   3017 Sep  7 15:22 fnord.txt
    -rw-r--r-- 1 yasiro01 Faculty   3340 Mar  2  2017 library_gen.ipynb
    -rw-r--r-- 1 yasiro01 Faculty  12021 Feb 20  2017 library.txt
    -rw-r--r-- 1 yasiro01 Faculty  19671 Sep  8 13:02 linux_commands.ipynb
    -rw-r--r-- 1 yasiro01 Faculty   8386 Sep  8 12:43 linux_commands.md
    -rw-r--r-- 1 yasiro01 Faculty      0 Sep  8 13:02 new_file
    -rw-r--r-- 1 yasiro01 Faculty   3943 Aug 12 19:04 passwd_gen.ipynb
    -rw-r--r-- 1 yasiro01 Faculty    467 Aug 13 20:59 roster.txt
    -rw-r--r-- 1 yasiro01 Faculty 938848 Sep  8 12:57 sorted_words
    ---
    total 984 -rw-r--r-- 1 yasiro01 Faculty 49 Sep 8 13:02 example.txt -rw-r--r-- 1 yasiro01 Faculty 3017 Sep 7 15:22 fnord.txt -rw-r--r-- 1 yasiro01 Faculty 3340 Mar 2 2017 library_gen.ipynb -rw-r--r-- 1 yasiro01 Faculty 12021 Feb 20 2017 library.txt -rw-r--r-- 1 yasiro01 Faculty 19671 Sep 8 13:02 linux_commands.ipynb -rw-r--r-- 1 yasiro01 Faculty 8386 Sep 8 12:43 linux_commands.md -rw-r--r-- 1 yasiro01 Faculty 0 Sep 8 13:02 new_file -rw-r--r-- 1 yasiro01 Faculty 3943 Aug 12 19:04 passwd_gen.ipynb -rw-r--r-- 1 yasiro01 Faculty 467 Aug 13 20:59 roster.txt -rw-r--r-- 1 yasiro01 Faculty 938848 Sep 8 12:57 sorted_words
    ---
    11
    ---
    11 - 1
    ---
    10



```bash
%%bash
# Display number of files in a directory by counting lines and subtracting 1
echo `ls -l | wc -l` - 1 | bc
```

    10



```bash
%%bash
sort /usr/share/dict/words > sorted_words
tr 'A-Z' 'a-z' < fnord.txt | tr -cs 'a-z' '\n' | sort | uniq | comm -23 - sorted_words
```

    
    alucard
    american
    apr
    binky
    centere
    da
    etc
    fnord
    fnords
    hq
    inc
    madison
    poeple
    polyspock
    revultion
    ror
    sdbp
    shawn
    somthing
    texbooks
    tfile
    ya



```bash
%%bash
# Cleaning up for the next run
if [ -a example.txt ] ; then rm example.txt ; fi
if [ -a new_file ] ; then rm new_file ; fi
if [ -a sorted_words ] ; then rm sorted_words ; fi
```
