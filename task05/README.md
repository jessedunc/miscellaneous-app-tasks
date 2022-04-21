## Task 05

In the `core_props` of all our nodes, `id` should be a random 16-digit hex token unless otherwise specified. Hex digits are 0-9 and a-f. Write a function in Python that generates a 16-digit lowercase hexstring. 

This is an example function in Javascript:

```
getRandomToken = () => {
  let newId = uuidv4().substring(0,16).replace(/-/g,'')
}
```

This is an example function in Bash which also strips the trailing newline character `\n` and copies the result to the clipboard. 

```
openssl rand -hex 8 | tr -d '\n' | xclip -sel clip
```

**Basic Task**

Write a function in Python to generate this 16-digit hexstring. Using `uuidv4` is a good place to start.

Example strings:

```
021d1825d9d6a553
c20d1d16b8474f2a
f0ff5550cc5b936d
```

**Bonus Round**

Create a function that:
- takes an integer for the number of digits desired
- takes an array so the func can check that the created id doesn't already exist
- returns a unique hexstring of user-defined length
