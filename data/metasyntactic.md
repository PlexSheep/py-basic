# Metasyntactic variable

## Tools

From Wikipedia, the free encyclopedia
This article is about metasyntactic variables in computer science and programming. For metasyntactic 
variables as used in formal logic, see Metavariable (logic). For usage in spoken languages, see 
Placeholder name.

A metasyntactic variable is a specific word or set of words identified as a placeholder in computer 
science and specifically computer programming. These words are commonly found in source code and are 
intended to be modified or substituted before real-world usage. For example, foo and bar are used in 
over 330 Internet Engineering Task Force Requests for Comments, the documents which define 
foundational internet technologies like HTTP (web), TCP/IP, and email protocols.[1][2]

By mathematical analogy, a metasyntactic variable is a word that is a variable for other words, 
just as in algebra letters are used as variables for numbers.[1]

Metasyntactic variables are used to name entities such as variables, functions, and commands whose 
exact identity is unimportant and serve only to demonstrate a concept, which is useful for teaching 
programming.
Common metasyntactic variables

Due to English being the foundation-language, or lingua franca, of most computer programming 
languages, these variables are commonly seen even in programs and examples of programs written for other spoken-language audiences.

The typical names may depend however on the subculture that has developed around a given programming 
language.

## General usage

Metasyntactic variables used commonly across all programming languages include foobar, foo, bar, 
baz, qux, quux, corge, grault, garply, waldo, fred, plugh, xyzzy, and thud; several of these words 
are references to the game Colossal Cave Adventure.[1][3]

A complete reference can be found in a MIT Press book titled The Hacker's Dictionary.

## Japanese

In Japanese, the words hoge (ほげ)[4] and fuga (ふが) are commonly used, with other common words 
and variants being piyo (ぴよ), hogera (ほげら), and hogehoge (ほげほげ).[5][circular reference] 
The origin of hoge as a metasyntactic variable is not known, but it is believed to date to the early 
1980s.[5]

## French

In France, the word toto is widely used, with variants tata, titi, tutu as related placeholders. 
One commonly-raised source for the use of toto is a reference to the stock character used to tell 
jokes with Tête à Toto.[citation needed]

## Turkish

In Turkey, the words hede and hödö (usually spelt hodo due to ASCII-only naming constraints of 
programming languages) are well-known metasyntactic variables stemmed from popular humorous cartoon 
magazines of the 90's like LeMan. The words don't mean anything, and specifically used in place of 
things that don't mean anything. The terms have been popularized to the masses by the actor and 
stand-up comedian Cem Yılmaz in the late 90's and early 2000's.[6]

## Usage examples
A screenshot of a metasyntactic variable FOO assigned and echoed in an interactive shell session.

## C
See also: C programming language

In the following example the function name foo and the variable name bar are both metasyntactic 
variables. Lines beginning with // are comments.

```c
// The function named foo
int foo(void)
{
   // Declare the variable bar and set the value to 1
   int bar = 1;

   return bar;
}
```

## C++
See also: C++

Function prototypes with examples of different argument passing mechanisms:[7]

```cpp
void Foo(Fruit bar);
void Foo(Fruit* bar);
void Foo(const Fruit& bar);

Example showing the function overloading capabilities of the C++ language

void Foo(int bar);
void Foo(int bar, int baz);
void Foo(int bar, int baz, int qux);
```

## Python

Spam, ham, and eggs are the principal metasyntactic variables used in the Python programming 
language.[8] This is a reference to the famous comedy sketch, "Spam", by Monty Python, the eponym 
of the language.[9] In the following example spam, ham, and eggs are metasyntactic variables and 
lines beginning with # are comments.

```python
# Define a function named spam
def spam():

    # Define the variable ham
    ham = "Hello World!"

    # Define the variable eggs
    eggs = 1

    return
```

## IETF Requests for Comments

Both the IETF RFCs and computer programming languages are rendered in plain text, making it 
necessary to distinguish metasyntactic variables by a naming convention, since it would not be 
obvious from context.

Here is an example from the official IETF document explaining the e-mail protocols (from RFC 772 - 
cited in RFC 3092):

```text
 All is well; now the recipients can be specified.

     S: MRCP TO:<Foo@Y> <CRLF>
     R: 200 OK

     S: MRCP TO:<Raboof@Y> <CRLF>
     R: 553  No such user here

     S: MRCP TO:<bar@Y> <CRLF>
     R: 200 OK

     S: MRCP TO:<@Y,@X,fubar@Z> <CRLF>
     R: 200 OK

  Note that the failure of "Raboof" has no effect on the storage of
  mail for "Foo", "bar" or the mail to be forwarded to "fubar@Z"
  through host "X".
```

(The documentation for texinfo emphasizes the distinction between metavariables and mere variables 
used in a programming language being documented in some texinfo file as: "Use the @var command to 
indicate metasyntactic variables. A metasyntactic variable is something that stands for another 
piece of text. For example, you should use a metasyntactic variable in the documentation of a 
function to describe the arguments that are passed to that function. Do not use @var for the names 
of particular variables in programming languages. These are specific names from a program, so 
@code is correct for them."[10])

Another point reflected in the above example is the convention that a metavariable is to be 
uniformly substituted with the same instance in all its appearances in a given schema. This is in 
contrast with nonterminal symbols in formal grammars where the nonterminals on the right of a 
production can be substituted by different instances.[11]
Example data
SQL

It is common to use the name ACME in example SQL Databases and as placeholder company-name for the 
purpose of teaching. The term 'ACME Database' is commonly used to mean a training or example-only 
set of database data used solely for training or testing. ACME is also commonly used in 
documentation which shows SQL usage examples, a common practice with in many educational texts as 
well as technical documentation from companies such as Microsoft and Oracle.[12][13][14]
