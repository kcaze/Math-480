# 🤖 Math 480 - Computing and AI in Mathematics

This is repository contains the course materials for the course [Math 480 - Computing and AI in Mathematics](https://math.washington.edu/special-offerings#S1) taught by me during the Summer 2024 quarter at the University of Washington. The course is intended to be a crash course introduction to programming with AI assistance, training neural nets on mathematical data, and formalizing mathematical proofs using Lean.

Each assignment is self-contained in its own folder in this repository but you are recommended to go through the assignments in order. There is an associated `README.md` for each assignment with instructions for how to get started, along with some additional pedagogical material. If you are stuck or want to see a reference solution each assignment folder contains a `solutions/` folder that you can compare your implementation to.

Before you begin working through the assignments, I recommend setting up a Conda environment to help manage Python dependencies and installing either Codeium or Cursor so that you can try completing the assignments with AI assistance. 

## AI Tools

One unique aspect of this course is that students were allowed to use any resource to help them code their assignments, including AI tools. The goal is to gain experience in how to effectively use these tools, just as how many software engineers are more productive by leveraging IDE features such as autocomplete, go to definition, and find references/usages. I recommend choosing one of the following tools to use:

- [Codeium](https://codeium.com) is available as an extension for VS Code, Neovim, Emacs, and many other editors. Autocomplete, chat, and refactoring tools are free to use without limits, but you currently need to subscribe for GPT-4 access.
- [Cursor](https://www.cursor.com/) is a standalone editor forked off of VS Code. The free plan gives a limited number of autocomplete suggestions and commands per month. Subscribing gives unlimited access to completions and commands and uses GPT-4, GPT-4o, and Claude 3.5 Sonnet. You are also given a limited number of "fast" priority requests per month.

Both Codeium and Cursor give non-intrusive autocomplete suggestions that take into account your entire codebase as you write code. Additionally, you can highlight sections of your code that you would like to modify or refactor and use natural language to dictate a refactoring command. You can also ask either tool to explain parts of the code that you do not understand.
