# DroneEngage Wiki Organization

This document describes the organization and structure of the DroneEngage documentation wiki.

## Documentation Hierarchy

The wiki is organized into four main sections:

### 1. User Guides
Easy-to-follow guides for users and operators.

- **Getting Started** (`de-getting-started.rst`)
  - Installation guides
  - Quick start tutorials
  - Basic configuration

- **Web Client** (`webclient-*.rst`)
  - Web client configuration
  - Gamepad control
  - Servo control
  - Swarm operations
  - UDP telemetry

- **Scenarios** (`scenarios/`)
  - All-in-one setup
  - Camera names
  - Drone connection
  - Use case examples

### 2. Technical Documentation
In-depth technical documentation for developers and system administrators.

#### Server Components (`technicals/server/`)
- **System Architecture** (`de-system-architecture.md`)
  - Overall system architecture
  - Component interactions
  - Data flow diagrams

- **Authenticator** (`de-server-technicals-authenticator.md`)
  - Tech stack and architecture
  - Core components
  - Configuration
  - Development guide

- **Communication Server** (`de-server-technicals-communication.md`)
  - Tech stack and architecture
  - Message routing
  - S2S authentication
  - UDP proxy

- **API Endpoints** (`de-server-api-endpoints.md`)
  - REST API reference
  - Admin endpoints
  - Agent endpoints
  - Web endpoints

- **Authentication Flow** (`de-server-authentication-flow.md`)
  - Login card creation
  - Account operations
  - Hardware verification
  - S2S authentication

- **Configuration** (`de-server-configuration.md`)
  - Server settings
  - Account storage
  - S2S configuration
  - SSL/TLS setup

- **Database Schema** (`de-server-database-schema.md`)
  - File-based storage
  - MySQL schema
  - Database operations

- **Message Propagation** (`de-server-message-propagation.md`)
  - Mesh relay system
  - Loop prevention
  - Message routing types

- **S2S Authentication** (`de-server-s2s-authentication.md`)
  - Ed25519 key setup
  - Challenge-response flow
  - Security best practices

#### Communication Module (`technicals/communication/`)
- **Technical Overview** (`de-comm-technicals.rst`)
  - Tech stack and architecture
  - Core components
  - Build instructions

- **Plugin-Broker Architecture** (`de-comm-plugin-broker-architecture.md`)
  - Plugin side components
  - Broker side components
  - Communication flow
  - Thread architecture

- **Configuration System** (`de-comm-configuration-system.md`)
  - CConfigFile singleton
  - Configuration values
  - Usage patterns

#### Vision Pipeline (`technicals/vision/`)
Groups the video-processing modules that form the camera → tracker → AI
chain described in the workspace `AGENTS.md` (virtual-video-device
pipeline), one subfolder per module:

- `technicals/vision/camera/` — `drone_engage_camera_2025` (active)
- `technicals/vision/ir-camera/` — `IR/drone_engage_IR_camera` (active), plus its
  dependency library `IR/mi48_lib_c/` and the reference-only `IR/pysenxor-master/`,
  documented together in the same folder
- `technicals/vision/tracking/` — reserved, not yet built
- `technicals/vision/ai-detection/` — reserved, not yet built (covers both `yolo_ai` and `yolo_ai_generic`)

#### Plugins (`technicals/plugins/`)
Groups the hardware/radio plugin modules referenced from `de-plugins.md`,
one subfolder per module:

- `technicals/plugins/sdr/`, `technicals/plugins/gpio/`, `technicals/plugins/sound/` — active
- `technicals/plugins/viewlink/`, `technicals/plugins/p2p/` — reserved, not yet built

#### Ops Tools (`technicals/ops/`)
Groups dev/ops-only modules with no end-user-facing (Track U) page —
`de_bot`, `droneengage_telnet`, `droneengage_performance_monitor`,
`drone_engage_wifi_manager`.

See `MODULES_MANIFEST.md` for the authoritative per-module status,
source files, and sync state — check it before porting or updating any
module's docs, and update it after.

#### MAVLink Module (`technicals/mavlink/`)
- **Technical Overview** (`de-mavlink-technicals.rst`)
  - Tech stack and architecture
  - Key features
  - Vehicle types
  - Flight modes

- **Configuration System** (`de-mavlink-configuration-system.md`)
  - CConfigFile singleton
  - RC channel configuration
  - Tracking configuration
  - Network configuration

- **RC Sub-Action** (`de-mavlink-rc-sub-action.md`)
  - RC_SUB_ACTION enumeration
  - Remote control modes
  - Timeout handling

- **Rate Limit Effect** (`de-mavlink-rate-limit-effect.md`)
  - Tracking rate limiting
  - Kalman filter interaction
  - Configuration ranges

- **Joystick Guided Mode** (`de-mavlink-joystick-guided-mode.md`)
  - Guided mode control
  - Velocity setpoints
  - Safety features

### 3. API Documentation
Complete API references for all components.

- **REST APIs** (`technicals/server/de-server-api-endpoints.md`)
  - Authenticator API
  - Communication Server API
  - Error codes
  - Response formats

- **WebSocket APIs** (in component technical docs)
  - Message protocols
  - Connection handling
  - Event types

- **MAVLink APIs** (in MAVLink technical docs)
  - Message types
  - Vehicle commands
  - Telemetry formats

### 4. Architecture Documentation
System architecture and design documents.

- **System Architecture** (`technicals/de-system-architecture.md`)
  - High-level architecture
  - Component diagram
  - Data flow
  - Integration points

- **Communication Architecture** (`technicals/communication/de-comm-plugin-broker-architecture.md`)
  - Plugin-broker pattern
  - Message routing
  - UDP communication

- **Server Architecture** (in server technical docs)
  - Authenticator architecture
  - Communication Server architecture
  - S2S architecture

## Development Documentation

For developers contributing to DroneEngage:

- **Development Guide** (`de-dev.rst`)
  - Building code
  - Testing
  - Contributing guidelines

- **Custom Plugins** (`de-custom-plugins.md`)
  - C++ plugins
  - Node.js plugins
  - Python plugins

- **Databus** (`de-dev-databus.md`)
  - Inter-module communication
  - Message protocol
  - Plugin development

## Server Installation

Server deployment and installation guides:

- **Server Index** (`srv-index.rst`)
- **Authentication** (`srv-authentication.rst`)
- **Communication** (`srv-communication.rst`)
- **Installation** (`srv-install-*.rst`)

## Deprecated Documentation

A small number of pages document features that were actually removed
(not just renamed/moved) — currently only the old Andruav GCS-mode UI:

- `andruav-gcs.rst`, `andruav-gcs-telemetry.rst` — superseded by the
  WebClient (`webclient-whatis.rst`, `webclient-udp-telemetry.rst`).
  Linked from `obsolete-index.rst`, not from top-level nav.

## Markdown Cross-References — Use Plain Links Only

This project's `.md` files are parsed by **recommonmark**, not
MyST-parser (confirmed in `conf.py`: only `'recommonmark'` is in
`extensions`, no `AutoStructify` is registered). This matters a lot for
how you write cross-references in `.md` files:

- **Works:** plain Markdown links — `[Link text](target-doc)` or
  `[Link text](target-doc.md)`. recommonmark converts these into real
  docutils reference nodes that Sphinx resolves.
- **Silently broken:** MyST syntax — `` {doc}`Link text <target>` ``,
  `` {ref}`...` ``, fenced `` ```{toctree} ``` `` or `` ```{note} ```
  `` blocks, `` ```eval_rst `` blocks. None of these are recognized by
  recommonmark's plain `CommonMarkParser`. They render as **literal
  text on the page** (curly braces and all) — and because recommonmark
  never turns them into a reference node, Sphinx never even attempts to
  resolve them, so **no build warning is emitted either**. This is the
  most dangerous kind of bug here: it looks clean in the build log and
  is broken on every page that has it. (Found and fixed across 10 files
  in this exact way, 2026-09-04 — always spot-check the rendered HTML
  after touching a `.md` cross-reference, don't just trust a clean build log.)
- Toctree directives (`.. toctree::`) only work in `.rst` files in this
  project — no `.md` file anywhere in this repo has a working toctree.
  If a page needs one, either make it `.rst`, or add the child pages to
  an *existing* `.rst` toctree elsewhere (e.g. a parent index page).
- A plain link to a target whose page also declares a matching
  `.. _label:` (most pages do, matching their own slug) will trigger a
  `more than one target found for 'any' cross-reference` **warning** —
  this is expected and harmless: Sphinx's "any" role still resolves it
  to the correct document (verified empirically, not just assumed) and
  produces a working link. Don't switch to `{doc}` to silence this
  warning — that trade produces a broken link to make a harmless
  warning disappear.

## Navigation

The wiki uses a **single-source-of-truth** hierarchy. Each topic appears in exactly one toctree.

- **Main Index** (`index.rst`) - Root entry point with all top-level sections
- **DE Index** (`de-index.rst`) - DroneEngage operator manual, modules, and configuration
- **Server Index** (`srv-index.rst`) - Server deployment and administration
- **Developer Guide** (`de-dev.rst`) - All technical/deep-dive docs including system architecture, module technicals, and plugin development
- **Andruav Index** (`andruav-index.rst`) - Andruav (phone-based) product docs, sibling to DE Index
- **Obsolete Index** (`obsolete-index.rst`) - Deprecated pages (old Andruav GCS-mode UI only)
- **Glossary** (`glossary.rst`) - Terminology and definitions (shared, not duplicated)

## File Naming Conventions

- User guides: `de-*.rst` or `de-*.md`
- Technical docs: `technicals/[component]/de-[component]-[topic].md`
- Vision pipeline docs: `technicals/vision/[module]/de-vision-[module]-technicals-[topic].md`
- Plugin docs: `technicals/plugins/[module]/de-plugins-[module]-technicals-[topic].md`
- Ops tool docs: `technicals/ops/[module]/de-ops-[module]-technicals-[topic].md`
- API docs: `de-server-api-endpoints.md`
- Architecture: `de-system-architecture.md`
- Server docs: `srv-*.rst`
- Web client docs: `webclient-*.rst`

## Updating Documentation

When adding new documentation:

1. Determine the appropriate section (User Guides, Technical, API, Architecture)
2. Follow the naming convention for that section
3. Update the relevant index file
4. Add cross-references to related documents
5. Ensure consistent formatting and structure
6. **Never duplicate a topic across multiple toctree indexes** - each page should appear in exactly one toctree
7. When both `.rst` and `.md` versions exist, keep only the `.rst` version (Sphinx priority)
8. Check `MODULES_MANIFEST.md` first for the module's status and source files before writing anything
9. A page marked `:orphan:` (rst) or with a "Draft skeleton" note (md) is a structural placeholder — fill it from the source path noted in the file, then remove the orphan/draft marker and wire it into the relevant index's toctree in the same change
