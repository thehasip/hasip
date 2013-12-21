Hasip project structure
=======================

    ├── config
    │   └── items
    ├── docs
    │   ├── general
    │   ├── items
    │   ├── modules
    │   └── static_files
    ├── hasip
    │   └── lib
    │       ├── base
    │       │   ├── general
    │       │   └── modules
    │       └── modules
    ├── log
    └── tmp
        └── pids

`config`: configuration file which are used project wide
`config/items`: configuration file(s) for [items](docs/items/README_items.md)
`docs/*`: project documentation
`hasip`: main application directory
`hasip/lib/base/general`: classes which are used project wide
`hasip/lib/base/modules`: base / parent class definitions for modules
`hasip/lib/modules`: module files which are used within the [items](docs/items/README_items.md)
`log`, `tmp`: directory to keep logs and temp files
