# Linux Commands

Let's take a look at the commands you are expected to learn in this module. There are many excellent guides and tutorials on the subject and this document is meant to be the first step in your learning, not the last.

You should execute these commands in the terminal of your Ubuntu while reading. Note that all commands are prefixed with **$** to distinguish from the output.

## General

* `alias`
* `clear`
* `echo`
* `exit`
* `history`
* `less`
* `logout`
* `man`

`echo` can be used to print something to the standard output.

```bash
# This is a comment
$ echo Hello, world
Hello, world
```

The following commands produce the same output. You should use quotes (single, double, or none) consistently and don't mix them in the same script.

```bash
$ echo Hello, world
Hello, world
```

```bash
$ echo 'Hello, world'
Hello, world
```

```bash
$ echo "Hello, world"
Hello, world
```

You must enclose a single quote inside a double quote.

```bash
$ echo "Let's go!"
Let's go!
```

`man` is short for manual and it's a great source of knowledge about other commands.

```bash
$ man
What manual page do you want?
```

You have to specify the command in order to see its on-line reference manual.

```bash
$ man echo
...
 Manual page echo(1) line 1 (press h for help or q to quit)
...
```

You can use `alias` to create an alias for frequently used commands.

```bash
$ alias h=history
$ h
```

## Files and directories

* `cat`
* `cd`
* `chmod`
* `chown` (requires **sudo**)
* `cp`
* `find`
* `ls`
* `locate`
* `mkdir`
* `mv`
* `pwd`
* `rm`
* `rmdir`
* `tail`
* `touch`

You can use `find` to find a file by name in a specific directory.

```bash
$ find /usr -name american-english
/usr/share/dict/american-english
```

`find` is a powerful command with many options. Here is an example of using `find` to delete all empty files in the current directory.

```bash
$ find . -maxdepth 1 -type f -size 0 -delete
```

Another command to find files is `locate`.

```bash
$ locate american-english
/usr/share/dict/american-english
/usr/share/man/man5/american-english.5.gz
```

Print the name of the current (working) directory.

```bash
$ pwd
/home/yasiro01
```

Use `cd` to navigate between directories. Try executing `pwd` after each directory change or watch the command prompt.

Go to the root directory.

```bash
$ cd /
```

Go to the current user's home directory.

```bash
$ cd
```

Go to the current user's home directory.

```bash
$ cd ~
```

Go to the parent directory (up one level).

```bash
$ cd ..
```

Go to the specific subdirectory of the current one.

```bash
$ cd notes
```

`ls` is a powerful command with many options. You don't have to memorize all of them but rather refer to the manual if you encounter an unknown option in this guide.

List the content (files and directories) of the current directory.

```bash
$ ls
bash_scripts  input_files  notes  python_scripts  README.md
```

You can list the content of any directory by specifying its path. Here is a list of files in the root directory.

```bash
$ ls /
bin   cdrom  etc   initrd.img      lib    lib64   lost+found  mnt  proc  run   snap  sys  usr  vmlinuz
boot  dev    home  initrd.img.old  lib32  libx32  media       opt  root  sbin  srv   tmp  var  vmlinuz.old
```

List the content of the directory /home/yasiro01 in a long format.

```bash
$ ls -l /home/yasiro01
total 88
drwxrwxr-x 25 yasiro01 yasiro01 4096 Jul 23 11:16 Classes
drwxr-xr-x  2 yasiro01 yasiro01 4096 Jul 23 23:13 Desktop
drwxr-xr-x  2 yasiro01 yasiro01 4096 Jun 17 23:00 Documents
drwxr-xr-x  2 yasiro01 yasiro01 4096 Aug  7 13:11 Downloads
-rw-r--r--  1 yasiro01 yasiro01 8980 Nov 20  2016 examples.desktop
drwxrwxr-x  2 yasiro01 yasiro01 4096 Jun 17 23:01 Installs
drwxr-xr-x  2 yasiro01 yasiro01 4096 Nov 20  2016 Music
drwxrwxr-x  2 yasiro01 yasiro01 4096 Jun 17 16:41 NetBeansProjects
drwxr-xr-x  2 yasiro01 yasiro01 4096 Nov 20  2016 Pictures
drwxr-xr-x  2 yasiro01 yasiro01 4096 Nov 20  2016 Public
drwxrwxr-x  2 yasiro01 yasiro01 4096 Jun 17 17:30 PycharmProjects
-rw-r--r--  1 yasiro01 yasiro01 3216 Jul  7 20:50 requirements35.txt
-rw-r--r--  1 yasiro01 yasiro01 2382 Jul  7 20:50 requirements36.txt
-rw-r--r--  1 yasiro01 yasiro01 1901 Jul  7 20:50 requirements37.txt
drwxrwxr-x  3 yasiro01 yasiro01 4096 Feb 16 17:22 sketchbook
drwxr-xr-x  4 yasiro01 yasiro01 4096 Jun 17 16:49 snap
drwxrwxr-x 23 yasiro01 yasiro01 4096 Jul 13 02:03 Source
drwxrwxr-x 13 yasiro01 yasiro01 4096 Apr 14 10:29 Students
drwxr-xr-x  2 yasiro01 yasiro01 4096 Nov 20  2016 Templates
drwxr-xr-x  2 yasiro01 yasiro01 4096 Nov 20  2016 Videos
```

List all files and directories, including hidden (starting with .).

```bash
$ ls -a
```

Display information about a specific file.

```bash
$ ls -l README.md
-rw-rw-r-- 1 yasiro01 yasiro01 739 Jan 21 13:07 README.md
```

Display information about a non-existing file.

```bash
$ ls -l new_file
ls: cannot access 'new_file': No such file or directory
```

Use `touch` to create a new empty file.

```bash
$ touch new_file
ls -l new_file
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:20 new_file
```

Using `touch` on an existing file changes its access date/time.

Use `cp` to copy a file.

```bash
$ touch example.txt
$ cp example.txt another_example.txt
```

\* means any character(s). This command lists all files ending in **example.txt**.

```bash
$ ls -l *example.txt
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 another_example.txt
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
```

Move (or rename) a file.

```bash
$ mv another_example.txt yet_another_example.txt
$ ls -l *example.txt
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 yet_another_example.txt
```

Delete a file.

```bash
$ rm yet_another_example.txt
$ ls -l *example.txt
-rw-rw-r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
```

Remove a file forcefully (e.g. a read-only).

```bash
$ rm -f example.txt
```

Use `chmod` to change a file mode.

```bash
$ chmod 755 example.txt
$ ls -l example.txt
-rwxr-xr-x 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
```

Change file mode and make it read-only.

```bash
$ chmod -w example.txt
$ ls -l example.txt
-r-xr-xr-x 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
```

Numeric representation of the mode.

```bash
$ chmod 644 example.txt
$ ls -l example.txt
-rw-r--r-- 1 yasiro01 yasiro01 0 Jan 21 14:31 example.txt
```

Change file mode and make it **executable**.

```bash
$ touch test_chmod
$ chmod +x test_chmod
$ ls -l test_chmod
-rwxr-xr-x 1 yasiro01 Faculty 0 Sep 27 21:10 test_chmod
```

Create (make) a new directory.

```bash
$ mkdir new_dir
$ touch new_dir/new_file
$ ls new_dir
new_file
```

Delete (remove) a directory.

```bash
$ rm -rf new_dir
```

**DANGER**: use `rm -rf` with great caution as it recursively removes the specified directory without any additional prompt.

Stop everyone from seeing the files in the directory *test_chmod*.

```bash
$ chmod -r test_chmod
$ ls test_chmod
ls: cannot open directory 'test_chmod': Permission denied
```

Stop everyone from going into the directory *test_chmod*.

```bash
$ chmod -x test_chmod
$ cd test_chmod
/bin/sh: 1: cd: can't cd to test_chmod
```

## User management

* `adduser` (requires **sudo**)
* `deluser` (requires **sudo**)
* `groups`
* `passwd`
* `usermod` (requires **sudo**)
* `w`
* `who`
* `whoami`

See your username.

```bash
$ whoami
yasiro01
```

Display groups the user belongs to.

```bash
$ groups yasiro01
yasiro01 : yasiro01 adm cdrom sudo dip plugdev lpadmin sambashare wireshark docker
```

See logged in users.

```bash
$ who
yasiro01 :0           2019-08-04 19:37 (:0)
```

See logged in users and their activity.
```bash
$ w
14:44:53 up 9 days,  3:50,  1 user,  load average: 1.16, 0.87, 0.83
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
yasiro01 :0       :0               12Jan19 ?xdm?   4:26m  0.01s /usr/lib/gdm3/gdm-x-session --run-script env GNOME_SHELL_SESSION_MODE=ubuntu gnome-session --session=ubuntu
```

## System

* `date`
* `shutdown`
* `uname`
* `uptime`
* `which`

Print the name of the system.

```bash
$ uname -a
Linux ubuntu 4.15.0-43-generic #46-Ubuntu SMP Thu Dec 6 14:45:28 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```

```bash
$ lsb_release -d -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.3 LTS
Release:	18.04
Codename:	bionic
```

Print the date and time of the system.

```bash
$ date
Wed Aug 14 18:18:25 CDT 2019
```

Print the system's uptime.

```bash
$ uptime
 18:18:47 up 9 days, 22:43,  1 user,  load average: 0.81, 0.73, 0.57
```


Print the path to the application by its name.

```bash
$ which python
/usr/bin/python
```

**ADVANCED**: use `lscpu`, `lshw`, `lslogins`, `lsmem`, `lspci`, and others starting with *ls* to display detailed information about your machine's subsystems.

## Process management

* `kill`
* `ps`
* `top`
* `htop`

See processes and sort them by memory usage (`head` cuts output after 10 lines).

```bash
$ ps -f --sort=-rss | head -n 10

UID        PID  PPID  C STIME TTY          TIME CMD
yasiro01 23106 23105  0 21:10 pts/78   00:00:00 ps -f --sort=-rss
yasiro01 23105 23078  0 21:10 pts/78   00:00:00 /bin/sh -c ps -f --sort=-rss | head -n 10
yasiro01 23107 23105  0 21:10 pts/78   00:00:00 head -n 10
```

See processes from all users and sort them by memory usage (`head` cuts output after 10 lines)
```bash
$ ps -lfy --sort=-time | head -n 10

S UID        PID  PPID  C PRI  NI   RSS    SZ WCHAN  STIME TTY          TIME CMD
S yasiro01 23108 23078  0  80   0   752  1127 wait   21:10 pts/78   00:00:00 /bin/sh -c ps -lfy --sort=-time | head -n 10
R yasiro01 23109 23108  0  80   0  1440  7282 -      21:10 pts/78   00:00:00 ps -lfy --sort=-time
S yasiro01 23110 23108  0  80   0   684  1826 pipe_w 21:10 pts/78   00:00:00 head -n 10
```

## Networking

* `ifconfig`
* `ip`
* `nslookup`
* `ping`

Network interface configuration, *lo* is a local loopback interface.

```bash
$ ifconfig lo
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 701224  bytes 264763645 (264.7 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 701224  bytes 264763645 (264.7 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## Tools

* `bc`
* `comm`
* `cut`
* `sort`
* `tr`
* `uniq`
* `wc`

## Pipes and redirection

* Backtick: \`
* Pipe (send output of one command to the input of another): |
* Redirect input: < (e.g. read from a file instead of standard input *stdin*)
* Redirect output: > (e.g. write output to a file instead of standard output *stdout*)
* Redirect output and append: >> (e.g. append output to a file)
* Redirect standard output stream: 1>
* Redirect standard error stream: 2>

Display the result of a command execution.

```bash
$ whoami
yasiro01
```

Display the result of a command execution. **Wrong way**.

```bash
$ echo whoami
whoami
```

Ticks allow you to use the result of a command execution.

```bash
$ echo `whoami`
yasiro01
```

Write hello world to a file.

```bash
$ echo hello world > example.txt
```

Append current date (result of the date command) to a file at the second line.

```bash
$ echo today is `date` >> example.txt
```

Display file content.

```bash
$ cat example.txt
hello world
today is Mon Jan 21 14:53:12 CST 2019
```

Display number of lines in a file.

```bash
$ cat example.txt | wc
2      10      49
```

`wc` use on its own produces similar, yet slightly different output.

```bash
$ wc example.txt
2 10 50 example.txt
```

Redirect default output to *mystery.txt*. The content of *mystery.txt* is the output of the command `find fnord.txt`.

```bash
$ find fnord.txt 1> mystery.txt
$ cat mystery.txt
fnord.txt
```

Map (translate) set of characters to something else.

```bash
$ echo 'Hello World' | tr 'a-k' 'A-K'
HEllo WorlD
```

Simple bash calculator `bc` can be used in interactive mode and in a script (pipe).

```bash
$ echo 2*2 | bc
4
```

```bash
$ echo 2^3 | bc
8
```

```bash
$ echo 160 / 10 | bc
16
```

Display number of files in a directory by counting lines and subtracting 1.

Let's take the result of `ls` piped to `wc`, create a subtraction expression, and pipe it to `bc`.

```bash
$ echo `ls -l | wc -l` - 1 | bc
7
```

Of course, `ls | wc -l` produces the same result.

Let's find all words in the file *fnord.txt* that are not in the built-in dictionary.

The solution uses commands `tr`, `sort`, `uniq`, and `comm`. Look them up.

```bash
$ sort /usr/share/dict/words > sorted_words
$ tr 'A-Z' 'a-z' < fnord.txt | tr -cs 'a-z' '\n' | sort | uniq | comm -23 - sorted_words
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
```

List all files in a directory and its subdirectories, sorting them by size.

```bash
$ ls -alRS | head -n 10
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
```

Count number of files in a directory and its subdirectories. All errors are sent to */dev/null*.

```bash
$ ls -AR 2>/dev/null | wc -l
235
```

Find all files with permission **777**. All errors are sent to */dev/null*.

```bash
find / -perm 777 2> /dev/null
```

## References

* [Basic Linux Commands](http://www.debianhelp.co.uk/commands.htm)
* [Basic UNIX commands](http://mally.stanford.edu/~sr/computing/basic-unix.html)
* [UNIX command summary](http://www.bsd.org/unixcmds.html)
* [Unix Commands](https://pangea.stanford.edu/computing/unix/shell/commands.php)
* [Introduction to Unix commands](https://kb.iu.edu/d/afsk)
* [50 Most Frequently Used UNIX / Linux Commands (With Examples)](http://www.thegeekstuff.com/2010/11/50-linux-commands/)
* [An Introduction to Linux I/O Redirection | DigitalOcean](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)
* [All about pipes, by The Linux Information Project (LINFO)](http://www.linfo.org/pipes.html)
* [Linux Tutorial - 11. Learn Piping and Redirection](https://ryanstutorials.net/linuxtutorial/piping.php)
* [Understanding Pipes and Redirection For the Linux Command Line](https://www.maketecheasier.com/pipes-redirection-for-linux-command-line/)
* [bc command in Linux with examples - GeeksforGeeks](https://www.geeksforgeeks.org/bc-command-linux-examples/)
* [How to Use the "bc" Calculator in Scripts](https://www.lifewire.com/use-the-bc-calculator-in-scripts-2200588)
* [bc Command Manual](https://www.gnu.org/software/bc/manual/html_mono/bc.html)
