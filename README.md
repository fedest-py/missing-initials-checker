# missing-initials-checker

This Python script identifies which letters of the alphabet were **not used as initials** among a group of user-provided names.

##  How it works:
1. The user inputs a list of names, separated by spaces.
2. The program collects the first letter of each name.
3. It compares these letters to the alphabet to determine which letters were **not used as initials**.
4. Missing letters are printed in alphabetical order.

## Example:
- Enter some names on a single line: charlie xavier bob thomas frank

- Missing Letters: a d e g h i j k l m n o p q r s u v w y z

## Concepts Demonstrated:
- String parsing and `.split()`
- List iteration and filtering
- Comparison with static reference list (`a` to `z`)
