# Package Structure

## Project Root
```
resume/
├── Resume Project Context Digest.md   # Project documentation and design decisions
├── resume.json                         # Structured resume data (JSON schema)
├── resume-renderer.html                # Self-contained HTML/CSS/JS renderer
├── serve.py                            # Local dev server (Python, zero dependencies)
└── .memory-bank/                       # Memory bank (this directory)
    ├── projectbrief.md
    ├── packageStructure.md
    ├── productContext.md
    ├── systemPatterns.md
    ├── techContext.md
    ├── activeContext.md
    └── progress.md
```

## File Descriptions

| File | Purpose | Format |
|------|---------|--------|
| `Resume Project Context Digest.md` | Comprehensive project documentation: schema, design decisions, usage instructions, future plans | Markdown |
| `resume.json` | Resume content data: personal info, profile, skills, experience, education | JSON |
| `resume-renderer.html` | All-in-one viewer: embedded CSS styling, JS rendering logic, and a copy of resume data | HTML/CSS/JS |
| `serve.py` | Local HTTP server — maps `/` to `resume-renderer.html`, default port 8000, stdlib only | Python 3 |

## Planned Future Structure
```
resume/
├── data/
│   └── resume-data.json
├── styles/
│   ├── modern.css
│   ├── traditional.css
│   └── minimal.css
├── resume-renderer.html
└── README.md
```

## Notes
- This is a standalone project, not a Brazil workspace
- No `node_modules`, build tools, or package managers involved
- The HTML renderer currently embeds a copy of the JSON data inline in a `<script>` tag
- `resume.json` exists as the canonical data source, but the renderer uses its own embedded copy
