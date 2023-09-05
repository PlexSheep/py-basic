# Tasks for beginners

This document contains some tasks for Python beginners. It does not aim to teach general 
programming techniques, only how to use Python. I try to avoid unrealistic tasks.

In case you have somehow gotten this document from another source, 
[this](https://git.cscherr.de/PlexSheep/py-basic/src/branch/master/Tasks.md) is the original 
source, where the links should hopefully work. If something does not work feel free to contact 
me at [software@cscherr.de](mailto:admin@cscherr.de).

## MD5 Hashchecker

### A. Produce a single MD5 Hash

Difficulty: 1/5

1. Hash the string `foobar19` with the MD5 hashing algorithm.

<details>
<summary>Hints</summary>

- Use Pythons `hashlib`.
- Your hashing function does not take strings for input, only raw data (bytes).
- You need to explicitly tell your hash to actually process the input.
- When printing your results, the result may be interpreted as data for characters. 
  You want the numeric value of the result in Hexadecimal.

</details>
<details>
<summary>Solution</summary>

The MD5 hash of `foobar19` is `fa5c65d5438f849387d3fdda2be4dd65`.

[Example Code](src/md5.py)

</details>

### B. Hash multiple values and search for specific ones.

Difficulty: 2/5

1. Find a way to produce strings with the basis `foobar` with appended numbers from `000000` to 
`999999`.

```text
1.      `foobar000000`
2.      `foobar000001`
3.      `foobar000002`
        ...
999998. `foobar999998`
999999. `foobar999999`
```

2. Hash all these with the MD5 hashing algorithm.
3. Find the exact numbers, how many of these hashes start with `00`
4. **Bonus**: 
    1. If MD5 was a good / perfect Hashing algorithm (it is definitely not), 
       how many matches for a `00` prefix should exist? Why?
    2. How many matches for $0$ to $50000$? How many matches for $0$ to $50.000.000$?

<details>
<summary>Testvectors</summary>

Last 5 Matches

```text
999384 | 009671fd23fa783df1fff63516e5d115
999751 | 00ec2ade58f75c44b7300294497f7fb1
999844 | 009cfd7949b577a3311d9db3ee49c15d
999852 | 006fe04f7d3f710f93d3e6324506154a
999902 | 00c063364ddffa1bdf338dfcf0319424
```

</details>
<details>
<summary>Hints</summary>

- Use a for loop to do the thing X times
- Use Pythons string formatting to put the numbers and string together
- Use Options for the `%d` Placeholder to get $0$ to be displayed as `000000`
- After hashing, check if your current hash matches the search. 
  Print it if that is the case to see if the match is a false positive.
- Increment a number on each match. The value of that number after the loop is how many
  Hashes start with `00` for this task.

</details>
<details>
<summary>Solution</summary>

There are 3889 hashes for `foobar000000` to `foobar999999` that produce an MD5 Hash that starts 
with `00`.

[Code Example](src/md5range.py)

**Bonus** 
We want $N/16^2$ occurrences for an ideal hashing algorithm, where $N$ is the maximum of our range 
$+ 1$. 

$16^2$ comes from $2$ characters in a range of `0` to `e` (Hexadecimal).

We want the hashing algorithm to spread out as much as possible, no value should be more common 
than any other value. This is essential for the security of the hashing algorithm. 

| Value        | Ideal Occurences |
|--------------|------------------|
| $1.000.000$  | $\approx 3906$   |
| $500.000$    | $\approx 1953$   |
| $50.000.000$ | $\approx 195312$ |

</details>

### C. Find earliest hash that fits criteria

Difficulty: 2/5

1. Find the earliest integer $X$ for `foobarXXXXXX` (where $X$ is an iterator as in the last 
subtask) that produces an MD5 hash that starts with `2718`.

<details>
<summary>Hints</summary>

- You can reuse most code from the last subtask.
- Match against the new prefix, but stop when you find it. 
- Display the index number in each loop iteration.

</details>
<details>
<summary>Solution</summary>

The first hash with prefix `2718` occurs at $i=70559$.

```text
070559 | 2718e5ee6d05091ce6dad023e55ee19c
```

[Code Example](src/md5range-4.py)

</details>

## Super basic web server

Difficulty: 3/5

1. Program a Python web server that writes "Python is not so hard" in your Browser (or in `cURL`).
   Use `http.server`.

<details>
<summary>Hints</summary>

- Use `http.server.SimpleHTTPRequestHandler` and `io.BytesIO`.
- Define your own class that inherits `SimpleHTTPRequestHandler`.
- You don't need to implement `do_GET()`.
- Implement your own `send_head()` method. This is the method that writes your response (not 
  completely on it's own, but unless you feel like inspecting standard libraries, just do what 
  I'm saying.).
- `send_head()` should take no arguments (other than `self`) and return some readable buffer.
- Don't forget to set the headers for HTTP before sending the body.
- Your OS might block hosting to ports < 1000. Try to host your web server to `localhost:8080`.

</details>
<details>
<summary>Solution</summary>

Take a look at the provided Code Example.

[Code Example](src/miniweb.py)

</details>

## Random Password generator

Difficulty: 2/5

1. Generate a string of 16 random alphanumeric characters.
2. When starting your script, take a number for a CLI Argument. Generate a random string of this 
   length.
3. **Bonus**
    - How many possible strings consisting of 16 alphanumeric characters can exist?
    - Add the possibility for a second argument `-v` that indicates your script should be more 
      verbose.
    - print the security bits ($log_2(L)$ where $L$ is the total number of possibilites) when the 
      `-v` flag is applied

Example:

```bash
$ python ./randomString.py 60
n51uxDLu3BnxZ1D00gYKYRcG2jh1Y6uulHgrJ0TK3w5FtWl6wm8U0azNtxw0
# ^^^^ the above is 60 characters ^^^^
```

<details>
<summary>Hints</summary>

- Use `random.choice` to generate a random character
- build your own alphabet string
- Use `sys.argv` to access the CLI Arguments

</details>
<details>
<summary>Solution</summary>

Take a look at the provided Code Example.

[Code Example](src/randomString.py)

**Bonus**

There are 62 alphanumeric characters (A-Z), (a-z), (0-9).

With $N$ characters, there are $62^N$ possible variants.
For $N=16$ that's $62^{16} = 47.672.401.706.823.533.450.263.330.816$ possible variants.

Security people measure security in Bits ($2^x$). You can calculate the bits of security with the 
logarithm base 2.

$S = log_2(62^N)$. 

We can immediately see that longer passwords are *exponentially* more secure than
more complex passwords (passwords that make use of complicated characters). For each bit, the 
security of the password is doubled.

For our example of $N=16$ we can calculate the security of the password like this:

$S=log_2(62^{16}) \approx 95.27$

That number of security bits is pretty good for passwords. However it does not cost you anything to 
just make your passwords longer than that, and give attackers no chance to break them by brute 
force.

</details>

## String Parsing with Regular Expressions

Difficulty: 2/5

<details>
<summary>Text</summary>

The text is large, read it [here](data/metasyntactic.md) and find the raw text for your program 
[here](https://git.cscherr.de/PlexSheep/py-basic/raw/branch/master/data/metasyntactic.md).

</details>

1. Use a regular expression (regex) to find all instances of a lowercase character with a 
following vowel character, in which no 'x', z' or 'y' follows the vowel in the given Text.
It is not allowed to store the text in source code, you must load it from an outside source, 
such as a file.

Examples:

| Original | is Match? |
|----------|-----------|
| foo      | yes       |
| baz      | no        |
| qux      | no        |
| Foo      | no        |
| bAR      | yes       |
| far      | yes       |

A hint that you don't want to miss: 

Use [regex101.com](https://regex101.com) if you are not already a REGEX expert.

<details>
<summary>Hints</summary>

TODO

</details>
<details>
<summary>Solution</summary>

TODO

</details>
