# DroneEngage / Andruav Wiki — Modules Manifest

Single source of truth for keeping this wiki in sync with the module
repositories in `public_versions/drone_engage/` (and the sibling
`andruav_android_app` repo). Before porting or updating docs for a
module, check its row here first. After porting, update the row
(`Status`, `Last Synced`).

Do not read module source code to update docs — only each module's own
`README.md` and `wiki/` folder are authoritative for documentation
purposes (per project convention). The one standing exception is
`de_common/de_databus/messages.hpp`: it is the canonical protocol wire
format (every message type, annotated with direction/rate/discard
guidance from a 2026 audit) and is explicitly approved as a doc source
for `andruav-communication-protocol-messages.rst`. Treat any other
`.hpp`/`.cpp`/`.js`/`.py` source file as off-limits for doc generation
unless the user names it explicitly, the way messages.hpp was named here.

Conventions: **Track U** = user-facing page(s) (top-level `de-*` /
`andruav-*` / `srv-*` / `webclient-*`, easy-to-follow, feature-first).
**Track D** = `technicals/` page(s) (developer/tweaker: architecture,
config keys, build steps, message formats).

## Workspace-level source (AGENTS.md)

`drone_engage/AGENTS.md` is the workspace's own module inventory
(repository layout, build systems, per-module quick-reference table) —
it's worth periodically diffing against this manifest's row list to
catch new/removed modules, since it's maintained independently by
whoever is doing engineering work in the workspace. Last checked:
**2026-09-04** — found `servers/droneengage_server_common` (a shared
npm package for the 3 Node.js servers) had been added since the
2026-08-29 audit; added to this manifest and given a real (non-skeleton)
Track D page the same day.

## Active modules

| Module | Repo path | Track U page(s) | Track D folder | Source docs mined | Status | Last synced |
|---|---|---|---|---|---|---|
| de_comm | `drone_engage_communication_pro/` | de-what-is, de-index | `technicals/communication/` | `wiki/*.md` | done | pre-existing |
| de_mavlink | `drone_engage_mavlink/` | de-config-mavlink, andruav-* | `technicals/mavlink/` | `wiki/*.md` | done | pre-existing |
| webclient | `droneengage_webclient_react/` | webclient-*.rst | `technicals/webclient/` | `wiki/*.md` | done | pre-existing |
| webconnector | `droneengage_webclient_react/webconnector/` | — (dev/ops only) | `technicals/webclient/de-web-technicals-webconnector*.md` | `webconnector/wiki/README_*.md` | **skeleton** | 2026-08-29 |
| droneengage_server | `servers/droneengage_server/` | srv-communication | `technicals/server/` | `wiki/*.md` | done | pre-existing |
| droneengage_authenticator | `servers/droneengage_authenticator/` | srv-authentication | `technicals/server/` | `wiki/*.md` | done | pre-existing |
| droneengage_storage_server | `servers/droneengage_storage_server/` | — (needs a Track U page: not yet planned) | `technicals/server/de-server-technicals-storage-*.md` | `wiki/*.md` (8 files) | **skeleton** | 2026-08-29 |
| droneengage_server_plugins | `servers/droneengage_server_plugins/` | de-plugins.md (general) | `technicals/server/de-server-technicals-plugins.md` | `readme.md` | **skeleton** | 2026-08-29 |
| droneengage_server_common | `servers/droneengage_server_common/` | — (dev-only shared package, no Track U) | `technicals/server/de-server-technicals-common.md` | `README.md` | done | 2026-09-04 |
| de_common | `de_common/` | — | `technicals/de_common/`, `andruav-communication-protocol-messages.rst` (message type reference, generated from `de_databus/messages.hpp` doc comments) | `README.md`, `de_databus/messages.hpp` | done | 2026-08-29 |
| de_databus | `de_databus/` | — | de-dev-databus.md | `README.md` (+nodejs/python/examples) | partial | pre-existing |
| drone_engage_camera_2025 | `drone_engage_camera_2025/` | de-camera.md | `technicals/vision/camera/` | `wiki/*.md` (4 files) | **skeleton** | 2026-08-29 |
| drone_engage_sdr_module | `drone_engage_sdr_module/` | de-plugin-sdr.rst | `technicals/plugins/sdr/` | `README.md` (no wiki/) | **skeleton** | 2026-08-29 |
| drone_engage_rpi_gpio | `drone_engage_rpi_gpio/` | de-plugin-gpio.rst | `technicals/plugins/gpio/` | `README.md` (no wiki/) | **skeleton** | 2026-08-29 |
| drone_engage_sound_module | `drone_engage_sound_module/` | de-plugin-sound.rst | `technicals/plugins/sound/` | `README.md` (no wiki/) | **skeleton** | 2026-08-29 |
| de_bot | `de_bot/` | — (ops tool, no Track U) | `technicals/ops/bot/` | `README.md` | **skeleton** | 2026-08-29 |
| droneengage_telnet | `droneengage_telnet/` | — (ops tool, no Track U) | `technicals/ops/telnet/` | `README.md` | **skeleton** | 2026-08-29 |
| droneengage_performance_monitor | `servers/droneengage_performance_monitor/` | — (ops tool, no Track U) | `technicals/ops/performance-monitor/` | `README.md` | **skeleton** | 2026-08-29 |
| drone_engage_wifi_manager | `drone_engage_wifi_manager/` | de-rpi-image-tools-wifi.rst (RPi-image tool, different scope) | `technicals/ops/wifi-manager/` | none found — needs a source doc pass before content can be written | **skeleton, blocked** | 2026-08-29 |
| drone_engage_IR_camera | `IR/drone_engage_IR_camera/` | — (needs a Track U page: not yet planned) | `technicals/vision/ir-camera/` | `README.md` (no `wiki/`) | **skeleton** | 2026-08-29 |
| mi48_lib_c *(dependency of IR camera)* | `IR/mi48_lib_c/` | — (library, no Track U) | `technicals/vision/ir-camera/de-vision-ir-camera-technicals-mi48-lib*.md` | `README.md` + `examples/README.md` | **skeleton** | 2026-08-29 |
| pysenxor-master *(reference, not a build dep)* | `IR/pysenxor-master/` | — (library, no Track U) | `technicals/vision/ir-camera/de-vision-ir-camera-technicals-pysenxor.md` | `README.md` | **skeleton** | 2026-08-29 |

Note on the IR camera cluster: `IR/README.md` describes it as one system —
`drone_engage_IR_camera` (the module) is built against `mi48_lib_c` (its
direct C++ dependency, own git repo); `pysenxor-master` is a vendored
Python reference implementation of the same sensor protocol, not linked
into the C++ build. All three are documented together under
`technicals/vision/ir-camera/` rather than split across separate
folders, since a reader tweaking the IR module needs the dependency's
API right next to it.

## Reserved (excluded from current scope — placeholder only, no folder created)

| Module | Repo path | Planned Track D location | Notes |
|---|---|---|---|
| drone_engage_tracking | `drone_engage_tracking/` | `technicals/vision/tracking/` | has `wiki/` (2 files) ready when unblocked |
| drone_engage_yolo_ai | `drone_engage_yolo_ai/` | `technicals/vision/ai-detection/` | has `wiki/messages-documentation.md` |
| drone_engage_yolo_ai_generic | `drone_engage_yolo_ai_generic/` | `technicals/vision/ai-detection/` (shares folder with yolo_ai — IMX500 vs ONNX/RKNN variants) | has `wiki/messages-documentation.md` |
| drone_engage_viewlink_module | `drone_engage_viewlink_module/` | `technicals/plugins/viewlink/` | no `wiki/`, no README found |
| drone_engage_p2p | `drone_engage_p2p/` | `technicals/plugins/p2p/` | no `wiki/` found |

Do not create folders or pages for the above until they're explicitly
pulled off hold. When they are, `technicals/vision/` and
`technicals/plugins/` already exist as the parent groupings — just add
the sibling subfolder.

## Video channels

**Correction (2026-09-04, verified by actually visiting both channels
via their RSS feeds):** the original assumption of a clean split
("hefnysco/personal channel = Andruav only, @droneengage = everything
else") does **not** match reality. Do not rely on it.

- `youtube.com/@droneengage` (UCWJ9fIsu0vZyLyGu9-W2oiw, 46 subs, 39
  videos) — DroneEngage content: modules, servers, webclient.
- `youtube.com/@MohammadHefny_HefnySco` (UCaFxcG3PV8j3l61eUrDJ4Zg,
  personal channel) — as of this review, its 15 most recent uploads are
  almost entirely **DroneEngage** content too (often the exact same
  video re-uploaded under a different video ID/edit — e.g. "How to Use
  Full Screen Display with HUD Overlay" exists as both `Y2vY4JiyK3M`
  (@droneengage) and `SfwnhNuqkXg` (personal)). No Andruav-app-specific
  video was found in this channel's recent sample. Older/back-catalog
  Andruav videos may still exist further back in its history — RSS only
  surfaces the latest 15 — but this was not verified.
- The wiki's *existing* embedded IDs that were spot-checked against
  @droneengage's feed (`Q-OyRnisq8U`, `VgB98DvSreg`) both confirmed
  correct. Existing `andruav-*.rst` embeds were not independently
  re-verified against either channel in this pass.

**Action needed from the user before doing any further video-embedding
work**: which channel is actually canonical for which topic now that
the clean split assumption is wrong? Until answered, default to
whichever channel's copy of a given topic has the most views/is more
polished, and note the choice inline.

No video assignment tracking yet for the modules above — deferred to
the Phase 4 (video/diagram) pass, except:

- `DMLjc728vMQ` ("DroneEngage GPIO Module", @droneengage) — embedded in
  `de-plugin-gpio.rst` on 2026-09-04, user-supplied.

## "Attractive for non-technical readers" pass (2026-09-04)

User asked: make the user-facing (Track U) pages open with a video,
image, or diagram — never plain text — since "the wiki is very
technical, which is ok, but I want non-technical people to find it
attractive." Scope was explicitly confirmed with the user: **Track U
pages only** (`de-*.rst`, `andruav-*.rst`, `srv-*.rst`,
`webclient-*.rst`, `scenarios/`) — `technicals/` stays plain-text
reference material, untouched.

**Judgment call, not explicitly confirmed with the user:** treated
`de-dev*.rst` and `de-contributing.rst` as developer-audience despite
matching the `de-*.rst` glob, and left them plain-text (they're
effectively Track D content that never got moved under `technicals/`).
If this was wrong, say so and I'll redo them the same way as the rest.

**Moved an existing visual to the top of the page** (was present but
buried lower down):
- `de-install-unit.rst`, `srv-authentication.rst`, `srv-communication.rst`,
  `srv-admin-web-interface.rst`

**Added a newly-matched video** (picked from the @droneengage /
@MohammadHefny_HefnySco catalog by relevance + view count, per your
"my judgment" answer):
- `webclient-mobile.rst` → `cO7825pTuAs` ("DroneEngage WebClient Mobile")
- `webclient-swarm.rst` → `B3Oe41PHwRo` ("Mav3DMap V2 - Visualizing DroneEngage Swarm Operations")
- `de-getting-started-index.rst` → reused `Q-OyRnisq8U` (the same overview video already on `de-getting-started.rst`/`de-what-is.rst`) since this is the landing page one level up

**Added an existing screenshot as opener** (no matching video found):
- `andruav-faq.rst` → `andruav.png`, `de-faq.rst` → `de.png`
- `de-advanced.rst` → `de_board_labelled.png`
- `de-config-comm.rst` → `broker_diagram.png`
- `srv-Installation.rst` → `srv_rpi_deployment.png`
- `srv-index.rst` → `comm_server_config.png`
- `webclient-configuration.rst` → `gcs_screen.png`

**Generated a new lightweight diagram** (no existing image or video fit
at all): `de-plugin-sound.rst` → `images/diagrams_2026/sound_plugin_overview_2026.svg`
(WebClient → de_snd → Speaker, 3-box flow). Deliberately simpler/friendlier
than the 5 protocol-reference diagrams in the same folder — no message
IDs or field lists, this one's for a non-technical audience.

**Also fixed while in these files:** 4 wrong image `:alt:` texts on
`webclient-swarm.rst` (all four said "FPV Vertical & Horizontal",
copy-pasted from an unrelated page — corrected to describe what's
actually shown).

**Already compliant, no change needed** (my first-pass regex scan
flagged these as "no visual" but they aren't):
- `webclient-servo.rst` — already opens with an image via `|pic1|`
  substitution syntax, which the naive scan didn't catch.
- `andruav-advanced.rst` — a legacy "merged into de-advanced" redirect
  stub, not a real content page; still linked from `andruav-index.rst`'s
  toctree so intentionally left as-is (not marked `:orphan:` like the
  unlinked redirect stubs from the earlier pass).

**Intentionally left as reference-style text, no forced visual**
(judgment call): `andruav-communication-protocol-messages.rst` — it's a
raw protocol/message-ID reference despite living at the Track U path
level; forcing a dense technical diagram at the top wouldn't serve a
non-technical reader either way.

**Backlog — pages that would benefit from a dedicated video but have
none yet** (flagging for future filming, not blocking): `de-plugin-sound`
(diagram added as a stand-in), `webclient-configuration`,
`webclient-servo`, `de-config-comm`, `srv-Installation`, `srv-index`,
`andruav-faq`, `de-faq`, `de-advanced`. Also unused-but-catalogued
videos worth placing somewhere if a good page emerges: `qjVyVDqJ6To` /
`dngYBl_zfXM` (optical fiber connectivity — no dedicated networking
page exists yet), `9FCykA5E8iw` / `effnFOjC8uM` (Isolated vs VPN vs
Public server choice — could reinforce `srv-install-airgap.rst`, which
already has a different video), `fPMxayr-AA8` / `a0IeNGBgMBU` (5,000km
rover — check whether it duplicates whatever's already on
`use-cases/de-france-rover.rst`, not verified this pass).
