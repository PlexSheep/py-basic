# Tasks for beginners

This document contains some tasks for Python beginners. It does not aim to teach general 
programming techniques, only how to use Python.

## MD5 Hashchecker
- [ ] Hash `foobar19` with the md5 hashing algorithm
    - Hints:
        - Use Pythons `hashlib`.
        - Your hashing function does not take strings for input, only raw data (bytes).
        - You need to explicitly tell your hash to actually process the input.
        - When printing your results, the result may be interpreted as data for characters. 
          You want the numeric value of the result in Hexadecimal.
    - Results:
        - ||MD5 of `foobar19` is `fa5c65d5438f849387d3fdda2be4dd65`||
- [ ] 1. rotate the base string `foobar` with numbers from 0 to 999999 like this:
        1.      `foobar000000`
        2.      `foobar000001`
        3.      `foobar000002`
        ...
        999999. `foobar999999`
      2. Get the MD5 hash value for each of those
      3. How many of these start with `00`?
    - Hints:
        - Use a for loop to do the thing X times
        - Use Pythons string formatting to put the numbers and string together
        - Use Options for the `%d` Placeholder to get 0 to be displayed as `000000`
        - do the same hashing as in the previous task
        - After hashing, check if your current hash matches the search. 
          Print it if that is the case to see if the match is a false positive.
        - Increment a number on each match. The value of that number after the loop is how many
          Hashes start with `00` for this task.
    - Testvectors, the last 5 matches:
        ```text
        999384 | 009671fd23fa783df1fff63516e5d115
        999751 | 00ec2ade58f75c44b7300294497f7fb1
        999844 | 009cfd7949b577a3311d9db3ee49c15d
        999852 | 006fe04f7d3f710f93d3e6324506154a
        999902 | 00c063364ddffa1bdf338dfcf0319424
        ```
    - Results:
        - ||3889 matches for the search parameters.||
- [ ] Continuing from the previous task, what is the earliest value for `foobarXXXXXX` (where `X`
      is a substitute for the iterating numbers) where the hash starts with `0000`?
      - Hints:
        - Stop on the earliest match.
      - Results:
        - || 021820 | 00001c9393b83c8da0db478687211d1d ||

## Super basic webserver
- [ ] Make a webserver print "Schlangenjazz" when you connect to it
