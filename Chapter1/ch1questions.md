1. Which of the following are operators, and which are values?
    - \*: operator
    - 'hello': value
    - -88.8: value
    - \-: operator
    - /: operator
    - +: operator
    - 5: value
2. Which of the following is a variable, and which is a string?
    - spam: variable
    - 'spam': string
3. Name three data types.
    - int
    - float
    - string
4. What is an expression made up of? What do all expressions do?
    - values and operators
    - they will evaluate to a value with no operators
5. What is the difference between an expression and a statement?
    - an expression evaluates to a value. An expression itself doesn't tell the program to do anything (unless it is an error, which would implicitly force the program to stop whatever the heck it is doing and throw an error message.)
    - a statement tells the program to do something.
6. What does the variable bacon contain after the following code runs?

> bacon = 20
> bacon + 1

`bacon` will have the value 21.

7. What should the following two expressions evalue to?

> 'spam' + 'spamspam'
> 'spam'\*3

Both evaluate to `spamspamspam`.

8. Why is `eggs` a valid variable name while 100 is invalid?

- 100 is a value.

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
    - int, float, str, respectively.

10. Why does this expression cause an error? How can you fix it?

> 'I have eaten ' + 99 + ' burritos.'

99 is not a string, so you get a typeError.

> 'I have eaten ' + str(99) + ' burritos.'

This will evaluate to `I have eaten 99 burritos.`

**Extra Credit** Look up what the round() function does.
 
round(float, int) will round numbers to a particular decimal place. You can use negative numbers to round to the left of the decimal point, which is kind of interesting.

