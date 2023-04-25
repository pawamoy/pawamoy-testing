---
title: Getting started with Insiders
---

# Getting started with Insiders

Pawamoy Testing Insiders is a compatible drop-in replacement for Pawamoy Testing,
and can be installed similarly using [`pip`][pip] or [`git`][git].
Note that in order to access the Insiders  repository,
you need to [become an eligible sponsor] of @pawamoy on GitHub.

  [pip]: #with-pip
  [git]: #with-git
  [become an eligible sponsor]: index.md#how-to-become-a-sponsor

## Requirements

After you've been added to the list of collaborators and accepted the
repository invitation, the next step is to create a [personal access token] for
your GitHub account in order to access the Insiders repository programmatically 
(from the command line or GitHub Actions workflows):

1.  Go to https://github.com/settings/tokens
2.  Click on [Generate a new token]
3.  Enter a name and select the [`repo`][scopes] scope
4.  Generate the token and store it in a safe place

  [personal access token]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
  [Generate a new token]: https://github.com/settings/tokens/new
  [scopes]: https://docs.github.com/en/developers/apps/scopes-for-oauth-apps#available-scopes

## Installation

### with pip

Pawamoy Testing Insiders can be installed with `pip`:

``` sh
pip install git+https://${GH_TOKEN}@github.com/pawamoy-insiders/pawamoy-testing.git
```

The `GH_TOKEN` environment variable must be set to the value of the personal
access token you generated in the previous step. Note that the personal access
token must be kept secret at all times, as it allows the owner to access your
private repositories.

### with git

Of course, you can use Pawamoy Testing Insiders directly from `git`:

```
git clone git@github.com:pawamoy-insiders/pawamoy-testing.git pawamoy-testing
```

When cloning from `git`, the package must be installed:

```
pip install pawamoy-testing
```

  [GitHub Container Registry]: https://docs.github.com/en/packages/guides/about-github-container-registry
  [Fork the Insiders repository]: https://github.com/pawamoy-insiders/pawamoy-testing/fork
  [GitHub Actions]: https://docs.github.com/en/github/administering-a-repository/disabling-or-limiting-github-actions-for-a-repository
  [packages scope]: https://docs.github.com/en/developers/apps/scopes-for-oauth-apps#available-scopes
  [GitHub Actions secret]: https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository
  [Create a new release]: https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository#creating-a-release
  [Pull App]: https://github.com/apps/pull
  [publish]: https://github.com/pawamoy-insiders/pawamoy-testing/blob/master/.github/workflows/publish.yml

## Upgrading

When upgrading Insiders, you should always check the version of Material for
MkDocs which makes up the first part of the version qualifier, e.g.Insiders
`4.x.x` is currently based on `8.x.x`:

```
8.x.x-insiders-4.x.x
```

If the major version increased, it's a good idea to consult the [upgrade
guide] and go through the steps to ensure your configuration is up to date and
all necessary changes have been made. If you installed Insiders via `pip`, you
can upgrade your installation with the following command:

```
pip install --upgrade git+https://${GH_TOKEN}@github.com/pawamoy-insiders/pawamoy-testing.git
```

  [upgrade guide]: ../upgrade.md

## Caveats

This section describes some aspects to consider when using Insiders together
with Pawamoy Testing to ensure that users without access to Insiders can
still build your documentation.

### Built-in plugins

When using built-in plugins that are solely available via Insiders, it might be 
necessary to split the `mkdocs.yml` configuration into a base configuration, and
one with plugin overrides. Note that this is a limitation of MkDocs, which can
be mitigated by using [configuration inheritance]:

=== ":octicons-file-code-16: `mkdocs.insiders.yml`"

    ``` yaml
    INHERIT: mkdocs.yml
    plugins:
      - search
      - social
      - tags
    ```

=== ":octicons-file-code-16: `mkdocs.yml`"

    ``` yaml
    # Configuration with everything except Insiders plugins
    ```

Now, when you're in an environment with access to Insiders (e.g. in your CI
pipeline), you can build your documentation project with the following lines:

```
mkdocs build --config-file mkdocs.insiders.yml
```

!!! tip "Sharing plugin and extension configuration"

    If you want to share `plugins` or `markdown_extensions` between both
    configuration files `mkdocs.insiders.yml` and `mkdocs.yml`, you can use
    the alternative key-value syntax in both files. The above example would
    then look like:

    === ":octicons-file-code-16: `mkdocs.insiders.yml`"

        ``` yaml
        INHERIT: mkdocs.yml
        plugins:
          social: {}
        ```

    === ":octicons-file-code-16: `mkdocs.yml`"

        ``` yaml
        # Additional configuration above
        plugins:
          search: {}
          tags: {}
        ```


  [configuration inheritance]: https://www.mkdocs.org/user-guide/configuration/#configuration-inheritance
