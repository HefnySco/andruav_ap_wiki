# droneengage_server_common

Shared configuration loader, helpers, and utilities used by all three
DroneEngage Node.js servers — `droneengage_authenticator`,
`droneengage_server`, and `droneengage_storage_server`. Installed via a
git URL (no npm registry), pinned to a tag for reproducible builds:

```json
"droneengage_server_common": "git+ssh://git@github.com:DroneEngage/droneengage_server_common.git#v1.0.0"
```

The build host needs SSH key access to the GitHub repo.

## What it provides

- **Config loader factory** (`create(options)`, `lib/js_serverConfig.js`)
  — each server wraps it with its own `configDir` and optional
  `enableHashHandling` / `envOverrides`:

  ```js
  const common = require('droneengage_server_common');
  const path = require('path');

  module.exports = common.create({
      configDir: path.join(__dirname, '..'),
      enableHashHandling: true,   // process $$HASH$$('...') directives
      envOverrides: {
          'DE_MY_ENV': 'config_key',
          'DE_MY_FLAG': (cfg, val) => { cfg.flag = (val === '1'); }
      }
  });
  ```

  Handles JSON-with-comments parsing, the `server.config.local` override
  merge (below), and `$$HASH$$` directives.
- **`dumperror`** — error-printing helpers, keeping all historical API
  names (`dumperror`, `fn_dumperror`, `dumperror2`, `fn_dumpdebug`) so
  existing call sites in each server didn't need renaming.
- **`helpers.*`** — `stripJsonComments`, `args`, `strings`, `validation`,
  `colors`, `styleHelper`.
- **`configHandler`** — the `$$HASH$$('...')` bcrypt directive processor.
- **`password`** — bcrypt hash/verify with a legacy plaintext fallback.

## `server.config.local` override pattern

Each server loads `server.config`, then looks for a sibling
`server.config.local`. If present, its top-level keys are merged on top
(shallow merge — the same top-level-key-only rule the C++ modules use
via `de_common::CConfigFile::updateJSON` for their own
`de_<module>.local` overrides). The local file is git-ignored and
supports C-style comments, exactly like `server.config`. This mirrors
the WebClient's `config.local.json` pattern. `$$HASH$$` directives from
the local file are hashed in memory only — never persisted back to the
local file.

## Why a shared package

Before this package existed, the config-loading and error-printing code
was duplicated across `droneengage_authenticator`, `droneengage_server`,
and `droneengage_storage_server` independently. Centralizing it means a
fix or a new `envOverrides` capability lands in one place and is picked
up by all three servers on their next dependency bump — at the cost of
needing SSH access to a private repo during `npm install` on build hosts.

## Related

- [Authentication Server](de-server-technicals-authenticator)
- [Communication Server Internals](de-server-technicals-communication)
- [Storage Server: Configuration](de-server-technicals-storage-configuration)
