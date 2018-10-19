# How to contribute

Thanks for taking the time to contribute to this open source project 👍.

## Submitting changes

- Make sure you have a [GitHub account](https://github.com/signup/free).
- Fork this repository on GitHub.
- Create a feature branch from where you want to base your work.
  - This will almost always be the `master` branch.
  - Avoid working directly on the `master` branch.
- Make commits of logical and atomic units, with unit tests written where applicable using the [Pytest](https://pypi.org/project/pytest/) framework.
- Check for unnecessary whitespace with `git diff --check` before committing.
- When committing, always write a clear commit message. Larger changes should follow the below structure.

```shell
$ git commit -m "A brief summary of the commit
>
> A paragraph describing what changed and its impact."
```

- Push your changes to a feature branch in your fork of the repository.
- Open a GitHub pull request with a clear list of changes made (read more about [pull requests](http://help.github.com/pull-requests/)).

## Coding conventions

- [Black](https://github.com/ambv/black) should be used for formatting Python code.
- [Pyre](https://pyre-check.org/) should be used for type checking.

## Additional resources

- [GitHub documentation](https://help.github.com/)
- [GitHub pull request documentation](https://help.github.com/articles/creating-a-pull-request/)
