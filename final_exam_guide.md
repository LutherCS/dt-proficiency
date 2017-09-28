
# Software Development Tools (CS 165)

## Final Exam Guide

 * Linux/UNIX comands
 * Pipes and redirection
 * Scripts
 * Regular expressions
 * Remote access
 * Git

See [Linux commands](linux_commands.ipynb) for detailed comamnds guide


```python
# see processes and sort them by memory usage (head cuts output after 10 lines)
!ps -f --sort=-rss | head -n 10
```

    UID        PID  PPID  C STIME TTY          TIME CMD
    yasiro01 23106 23105  0 21:10 pts/78   00:00:00 ps -f --sort=-rss
    yasiro01 23105 23078  0 21:10 pts/78   00:00:00 /bin/sh -c ps -f --sort=-rss | head -n 10
    yasiro01 23107 23105  0 21:10 pts/78   00:00:00 head -n 10



```python
# see processes from all users and sort them by memory usage (head cuts output after 10 lines)
!ps -lfy --sort=-time | head -n 10
```

    S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
    S yasiro01 23108 23078  0  80   0   752  1127 wait   21:10 pts/78   00:00:00 /bin/sh -c ps -lfy --sort=-time | head -n 10
    R yasiro01 23109 23108  0  80   0  1440  7282 -      21:10 pts/78   00:00:00 ps -lfy --sort=-time
    S yasiro01 23110 23108  0  80   0   684  1826 pipe_w 21:10 pts/78   00:00:00 head -n 10



```python
# Network interface configuration, lo is a local loopback interface
!ifconfig lo
```

    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:145356737 errors:0 dropped:0 overruns:0 frame:0
              TX packets:145356737 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1 
              RX bytes:501623479400 (501.6 GB)  TX bytes:501623479400 (501.6 GB)
    



```python
# Redirect default output to mystery.txt. The content of mystery.txt is the output of the command find fnord.txt
!find fnord.txt 1> mystery.txt
!cat mystery.txt
!rm mystery.txt
```

    fnord.txt



```python
# Map (translate) set of characters to something else
!echo 'Hello World' | tr 'a-k' 'A-K'
```

    HEllo WorlD



```python
# List all files in a directory and its subdirectories, sorting them by size
!ls -alRS | head -n 10
```

    .:
    total 13976
    -rw-r--r-- 1 yasiro01 Faculty 13114317 Sep 26 12:39 pattern_matching.ipynb
    -rw-r--r-- 1 yasiro01 Faculty  1000969 Sep  8 23:38 linux_commands.ipynb
    -rw-r--r-- 1 yasiro01 Faculty    59245 Sep 26 12:17 error.log
    -rw-r--r-- 1 yasiro01 Faculty    37966 Sep 21 10:58 animals.txt
    -rw-r--r-- 1 yasiro01 Faculty    12021 Sep 20 13:08 library.txt
    -rw-r--r-- 1 yasiro01 Faculty    10226 Sep  8 13:03 linux_commands.md
    -rw-r--r-- 1 yasiro01 Faculty     8132 Sep 27 21:08 final_exam_guide.ipynb
    -rw-r--r-- 1 yasiro01 Faculty     7740 Sep 20 15:13 library_gen.ipynb
    ls: write error: Broken pipe



```python
# Count number of files in a directory and its subdirectories. All errors are sent to /dev/null
!ls -AR 2>/dev/null | wc -l
```

    235



```python
# Go to the root directory
!cd /
# Go to the home directory
!cd ~
# Go to the parent directory
!cd ..
# Go to the home directory
!cd
```


```python
# Create an empty file
!touch test_chmod.txt
!ls -l test_chmod.txt
```

    -rw-r--r-- 1 yasiro01 Faculty 0 Sep 27 21:10 test_chmod.txt



```python
# Change file mode and make it executable
!chmod +x test_chmod.txt
!ls -l test_chmod.txt
```

    -rwxr-xr-x 1 yasiro01 Faculty 0 Sep 27 21:10 test_chmod.txt



```python
# Change file mode and make it non-writable
!chmod -w test_chmod.txt
!ls -l test_chmod.txt
```

    -r-xr-xr-x 1 yasiro01 Faculty 0 Sep 27 21:10 test_chmod.txt



```python
# Remove a file by force (e.g. a read-only)
!rm -f test_chmod.txt
```


```python
# Directory permissions
!mkdir test_chmod
# Stop everyone from seeing the files in test_chmod
!chmod -r test_chmod
!ls test_chmod
# Stop everyone from going into test_chmod
!chmod -x test_chmod
!cd test_chmod
!rm -rf test_chmod
```

    ls: cannot open directory 'test_chmod': Permission denied
    /bin/sh: 1: cd: can't cd to test_chmod


### Pipes and redirection

 * Use << to redirect input from a file
 * Use > to redirect output to a file (overwrite)
 * Use >> to redirect output to a file (append)
 * Use command 1> file to send standard command output to a file
 * Use command 2> file to send error command output to a file
 * Use cat <file> | command to send content of the file to a command input

### Scripting

[Linux Shell Scripting Tutorial - A Beginner's handbook](http://www.freeos.com/guides/lsst/)

### Regex
[Regex Cheat Sheet](http://www.rexegg.com/regex-quickstart.html)
