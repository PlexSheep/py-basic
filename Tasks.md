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
    - print the security bits ($log_2(L)$ where $L$ is the total number of possibilities) when the
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

1. Use a regular expression (regex) to find all words that start with a lowercase character with a
following vowel character, in which no 'x', z' or 'y' follows the vowel in the given Text.
It is not allowed to store the text in source code, you must load it from an outside source,
such as a file.

Examples:

| Original | is Match? |
|----------|-----------|
| foo      | yes       |
| foobar   | yes       |
| tayfoo   | no        |
| baz      | no        |
| qux      | no        |
| Foo      | no        |
| bAR      | yes       |
| far      | yes       |

A hint that you don't want to miss:

Use [regex101.com](https://regex101.com) if you are not already a REGEX expert.

<details>
<summary>Hints</summary>

- use `open()` to open your file for reading.
- use the `read()` method to read the file out.
- Use the `re` library
- Use `\b` to match a word boundary
- Use ranges `[5-9]`
- You can set a higher precedence by putting things in braces `(ABC)`.
- You can connect two expressions with `A|B` to use either `A` or `B`
- Use global mode.

</details>
<details>
<summary>Solution</summary>

There should be $374$ matches.

A regex that matches the requirements is `\b[a-z][AEIOUaeiou]([a-w]|[A-W])`.

[Code Example](src/tasks/regex.py)

</details>

## Primitive Cryptography

This section covers some ancient and / or primitive methods of Cryptography.
These are relatively easy to code and give a basic understanding of used
concepts.

### A. The Caesar Cipher

Difficulty: 2/5

<details>
<summary>Text</summary>

```text
Gxhobf bl t kxytvmhk, tgw lhfxmbfxl kxwtvmhk, bg max mktwbmbhg hy Obf (pabva bmlxey wxkboxl ykhf
Lmxobx). Bm bl ghm t kxpkbmx unm t vhgmbgntmbhg tgw xqmxglbhg hy Obf. Ftgr vehgxl tgw wxkbotmboxl
xqblm, lhfx oxkr vexoxk—unm ghgx tkx Obf. Gxhobf bl unbem yhk nlxkl pah ptgm max zhhw itkml hy
Obf, tgw fhkx.
````

</details>

1. The text above has been cyphered with the Caesar cipher, a timeless,
   classical algorithm that abstracts the meaning of text away and arguably
   an early form of encryption. Your task is to decipher it back into readable
   text.
2. **Bonus**
    - What if you didn't just try all possible combinations? How could you find
        the key without trying until you find it?

**The cipher**

For the Caesar cipher, all letters are shifted by the value of the key.

**Examples**

`foo Bar` becomes `gpp Cbs` when shifted by $1$.

Try to find out the rest for yourself.

<details>
<summary>Hints</summary>

- You can use the `ascii` codes of the letters to your advantage.
- You need to distinguish between lower and upper case.
- To roll back from back from a too high index back into the range of real
    letters. To do that you can use the modulo operation, which computes the
    remainder of a division by x. This is actually finite field arithmetic,
    but don't get so deep into the math.
- It is handy to have a command line argument for key and source text.

</details>
<details>
<summary>Solution</summary>

I ciphered the text with the key $19$. The original, deciphered text is:

<details>
<summary>Text</summary>

```text
Neovim is a refactor, and sometimes redactor, in the tradition of Vim (which itself derives from
Stevie). It is not a rewrite but a continuation and extension of Vim. Many clones and derivatives
exist, some very clever—but none are Vim. Neovim is built for users who want the good parts of
Vim, and more.
````

</details>

To decipher, you just apply the shifting of number backwards, or with the key
$-19$ (that's the same thing!).

[Code Example](src/caesar.py)

**Bonus**
One other way you could try to *recover* the key with is by statistical
analysis. Western languages (like English, German, etc.) have some letters,
words, combinations of letters, that are more common than others. These follow
a [statistical distribution](https://en.wikipedia.org/wiki/Letter_frequency).
The letter that is by far the most common in English is `e`.

With this information, you could count the occurrences for each letter and find
that the graph of frequencies looks the same -- only shifted by a couple
letters. That difference is your key.

Another way to try to recover the key is by looking at obvious words. The second
word in the cipher text is a single `t`. How many (common) words do you know
that only have one letter? I only know `a`. If we calculate the difference,
again, we get $19$, which is the key.

</details>

## Making a Hexeditor

In this section, we're building a little hexeditor. You will be able to install
it on your system and use it instead of the `hexdump` and `xxd` built into most
Linux distributions.

Hexdumping is actually really simple, all you have to do is read a file and
print it's direct content interpreted as numbers in hexadecimal. Apply some
fancy string formatting and we're done!

The editing part is a lot harder. It requires us to build a functioning TUI -
Terminal User Interface, as working with command line arguments or regular
reading from stdin won't help us much for editing a file. (if that's your thing,
use `ed`.).

Note: If you're looking for a great, fully featured hexeditor, I'd recommend
`bvi` ("binary vi"), which is packaged by most distributions.

-> `apt-get install bvi` <-

Note: I have no Idea how to install a python script as executable on windows, I
don't like windows either, so no support for installing stuff on windows.

### A. Hexdumper
Difficulty: 3/5


1. Dump the data of [data/metasyntactic.md](./data/metasyntactic.md) -- In
   Hexadecimal.
2. Make the dumped Bytes look pretty, something like the example below:

<details>
    <summary>Hexdump Example Display</summary>

`data/metasyntactic.md` looks like this when hexdumped:

```text
Line      Data
=================================================
0000000 ┃ 6f4e 6574 203a 6854 7369 6920 2073 6874
0000010 ┃ 2065 6957 696b 6570 6964 2061 6170 6567
0000020 ┃ 6620 726f 6d20 7465 7361 6e79 6174 7463
0000030 ┃ 6369 7620 7261 6169 6c62 7365 6920 206e
0000040 ┃ 6e45 6c67 7369 2c68 3220 3230 2d33 3930
0000050 ┃ 302d 2e35 4620 6e69 2064 6874 0a65 7075
0000060 ┃ 7420 206f 6164 6574 6f20 6972 6967 616e
0000070 ┃ 206c 685b 7265 5d65 6828 7474 7370 2f3a
0000080 ┃ 652f 2e6e 6977 696b 6570 6964 2e61 726f
0000090 ┃ 2f67 6977 696b 4d2f 7465 7361 6e79 6174
00000a0 ┃ 7463 6369 765f 7261 6169 6c62 2965 0a2e
00000b0 ┃ 230a 4d20 7465 7361 6e79 6174 7463 6369
00000c0 ┃ 7620 7261 6169 6c62 0a65 230a 2023 6f54
00000d0 ┃ 6c6f 0a73 460a 6f72 206d 6957 696b 6570
00000e0 ┃ 6964 2c61 7420 6568 6620 6572 2065 6e65
00000f0 ┃ 7963 6c63 706f 6465 6169 540a 6968 2073
0000100 ┃ 7261 6974 6c63 2065 7369 6120 6f62 7475
0000110 ┃ 6d20 7465 7361 6e79 6174 7463 6369 7620
...
```
</details>
