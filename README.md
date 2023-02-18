# Kent Beck TDD Python
## Following the examples of TDD outlined in Kent Beck's book Test Driven Development

Kent Beck is the author of Test-Driven Development. A book outlining a style of development consisting of techniques which encourages simple design and inspires confidence. The ultimate goal of TDD is to release working software quickly and give developers peace of mind when making changes.

Due to its nature, TDD is extremely useful in an agile environment. You'll see how relying on these techniques, along with simple DevOps practices, software development can proceed smoothly.

## Mindset
Given some project, or some requirements. Ask yourself, "What set of tests, when passed, will demonstrate the presense of code we are confident will compute the desired output correctly?"

To answer these questions make a To-do list as a reminder of your goals

## Rules
The general rules of TDD.

1. Write a test. Write the code as it appears in your mind, define the perfect interface for your request. Include everything you think will be necessary to get the expected output.
2. Make it run. Quickly getting those green dots dominates everything else. If a clean, simple solution is obvious, the type it in. If the clean, simple solution is obvious but it will take you a minute, then make a note of it and get back to the main problem. which is getting the bar green in seconds. Quick green excuses all sins, but only for a moment.
2. Make it run. Getting green dots is the highest priority. Use clean simple solutions that take seconds should be used before solutions that take minutes. If something takes minutes, make a note of it and find something that takes seconds. Get green, but remember to revisit bad decisions.
3. Make it right. Once you have those green dots, make the solution a nice one! Remove any duplication.

# Part 1 Rules
1. Quickly add a little test.
2. Run all tests and see the new one fail.
3. Make a little change.
4. Run all tests and see them all succeed.
5. Refactor to remove duplication.
