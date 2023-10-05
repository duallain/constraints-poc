# constraints-poc

Goal is to make a little poc for myself to learn how to do constraint programming in python.

Primary interest is understanding how to optimize things like purchasing in idle games.
But I have almost zero experience with the underlying math and with the tools available, so this poc is just to get a handle on both.


# setup
trying to record for myself what I did, you may need to troubleshoot installs and such, but hopefully this can at least be a list of stuff to think about. 

`pip3 install -r requirements.txt`
`brew install cbc` (need a solver for pyomo, this one seemed to be 'free-est' available)

# resources

Book examples with or-tools is from "Practical Python AI Projects: Mathematical Models of Optimization Problems with Google OR-Tools" I'll call it 'practical' in docstrings for short


the pyomo examples are drawn from https://www.youtube.com/playlist?list=PLaoe2MTbJBvpFPyMMSOB-WrHofdHo3e74
a nice playlist from Mike Wagner.

# Using project

I setup a Makefile to do all the tasks I think will be nice to happen regularly.

This includes, running the unit tests (with coverage), formatting coverage for my vscode coverage plugin. formatting code (with black), generating documents (with spinx-apidoc)

# github actions

I'm experimenting with these a bit, but coverage/unittests pass/formatting is not needed should all work and results should be shown on prs.


# docs available

on github pages https://duallain.github.io/constraints-poc/
likely very threadbare, but easy to add new content! as an action builds and publishes these docs on merges to main


# todos

- [ ] follow some examples from the book "Practical Python AI Projects: Mathematical Models of Optimization Problems with Google OR-Tools"
- [ ] play with some type hinting in python
- [ ] play around with some performance measurements. Given some test inputs, which algo is fastest for example
- [ ] follow through on some possible projects: a. diet/food fill in, b. sheet good piece optimizer