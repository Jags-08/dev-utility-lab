# CLI Examples & Showcase

`dev-utility-lab` includes a versatile command-line application out of the box (`dev-utils`). Here are realistic terminal outputs exhibiting the operations available.

## Advanced Math: Factorial

Calculate massive permutations safely from your shell:

```bash
$ dev-utils factorial 10
3628800

$ dev-utils factorial 5
120
```

## Security: Password Generation

Need a secure, ephemeral password on the fly? Generate 16-character alphanumeric sequences instantly:

```bash
$ dev-utils generate-password --length 16
aV8N2jP9Xq4kL0mU

$ dev-utils generate-password --length 24
qW2eR5tY8uI1oP4aA7sD0fG3
```

## String Processing: Palindrome Check

A lightning-fast query to determine sequential equivalence, ignoring cases and spaces.

```bash
$ dev-utils palindrome-check "Racecar"
True

$ dev-utils palindrome-check "A man a plan a canal Panama"
True

$ dev-utils palindrome-check "Hello World"
False
```

## Data Integration: File Reading

Safely ingest small logs or simple text files into standard output for piping.

```bash
$ echo "Hello from dev-utility-lab!" > my-log.txt

$ dev-utils read-file my-log.txt
Hello from dev-utility-lab!
```
