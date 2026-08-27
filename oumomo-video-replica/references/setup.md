# Oumomo CLI Setup

Use this reference only when `oumomo-agent` is missing or not authenticated.

## Install

If `command -v oumomo-agent` fails, tell the user that the Oumomo CLI is
required, then run:

```bash
npm install -g oumomo-agent
```

Verify the installation:

```bash
oumomo-agent --version
```

## Authenticate

Check the session:

```bash
oumomo-agent auth status
```

If it is not authenticated, run:

```bash
oumomo-agent setup
```

This opens the Oumomo browser login. Wait for setup to finish before calling
business tools.

The current CLI does not provide `oumomo-agent login` or
`oumomo-agent auth login`. Do not invent or run either command.
