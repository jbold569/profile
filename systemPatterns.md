# System Patterns

## Architecture: Data/Presentation Separation

```
┌─────────────────┐       ┌──────────────────────────────┐
│  resume.json    │       │  resume-renderer.html         │
│  (Canonical     │──────▶│  ┌────────────────────────┐   │
│   Data Source)  │       │  │ Embedded CSS Styling    │   │
│                 │       │  ├────────────────────────┤   │
│                 │       │  │ JavaScript Renderer     │   │
│                 │       │  │ - formatDate()          │   │
│                 │       │  │ - renderResume()        │   │
│                 │       │  ├────────────────────────┤   │
│                 │       │  │ Inline resumeData copy  │   │
│                 │       │  └────────────────────────┘   │
└─────────────────┘       └──────────────────────────────┘
                                      │
                                      ▼
                          ┌──────────────────────┐
                          │  Browser Rendering    │
                          │  + Print-to-PDF       │
                          └──────────────────────┘
```

**Current pattern**: The renderer embeds a full copy of the resume data in a `<script>` block. The standalone `resume.json` file serves as the canonical source of truth, but edits must be manually synced into the renderer.

## Key Design Patterns

### 1. Schema-Driven Content
All resume content follows a strict JSON schema with typed fields:
- **ISO dates** (`YYYY-MM`) for consistent parsing and display
- **Boolean flags** (`current: true/false`) for role status
- **Nullable fields** (`null` for missing GPA, honors, dates)
- **Flexible arrays** (empty `[]` for future expansion of technical skills, technologies)

### 2. Combined Profile Section
Single `profile` string field replaces separate summary and objective sections:
- Leads with value proposition (who you are, what you bring)
- Follows with career goals
- More impactful for leadership-level resumes

### 3. Metrics-in-Highlights Pattern
Quantitative achievements are embedded directly in experience bullet points rather than stored in separate fields:
- "$7 million technology portfolio"
- "92% increase in logging coverage"
- "$1.3 million in savings annually"
- "98% coverage (~70k endpoints)"
- "$9 million in annual revenue"

This provides natural context alongside each achievement.

### 4. Skills Organization
```
skills/
├── certifications[]     # Formal certs with name, abbreviation, issuer, dates
├── knowledgeDomains[]   # High-level competency areas (strings)
└── technical/           # Granular technical skills (currently empty)
    ├── platforms[]
    ├── tools[]
    ├── languages[]
    └── frameworks[]
```
Certifications are under skills (not education) per user preference.

### 5. Rendering Pipeline
```
JSON Data → formatDate() → renderResume() → innerHTML injection → DOM Display
```
- `formatDate()`: Converts `YYYY-MM` to `Mon YYYY`, handles `null` → `"Present"`
- `renderResume()`: Builds complete HTML string using template literals
- Single DOM write via `container.innerHTML = html`

### 6. Print Optimization
Dedicated `@media print` CSS rules:
- Removes background colors and box shadows
- Adjusts padding for paper margins
- Prevents page breaks inside job entries and sections
- Full-width layout (removes max-width constraint)

### 7. Responsive Design
`@media (max-width: 768px)` breakpoint:
- Skills grid collapses from 2-column to 1-column
- Contact info stacks vertically
- Container padding reduces

## Component Relationships

| Component | Depends On | Produces |
|-----------|-----------|----------|
| `resume.json` | Nothing (canonical source) | Structured resume data |
| `resume-renderer.html` | Embedded copy of resume data | Browser-rendered resume, PDF via print |
| `Resume Project Context Digest.md` | Documents both above | Project documentation |
