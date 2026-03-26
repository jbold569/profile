# Tech Context

## Technologies Used

### Frontend (Renderer)
- **HTML5**: Semantic markup, single-page document
- **CSS3**: Flexbox, Grid (skills layout), media queries, print styles
- **Vanilla JavaScript**: Template literals for HTML generation, DOM manipulation
- **No frameworks or build tools**: Zero dependencies, fully self-contained

### Data Format
- **JSON**: Structured resume data with typed fields
- **Schema conventions**: ISO date format (`YYYY-MM`), nullable fields, boolean flags, nested objects

### Typography & Visual Design
- **Primary font**: Segoe UI → Tahoma → Geneva → Verdana → sans-serif (fallback chain)
- **Header color**: Navy blue `#2c3e50`
- **Accent color**: Light blue `#3498db`
- **Body text**: `#333` (dark gray), `#555` (medium gray for secondary)
- **Layout**: Single column, `max-width: 850px`, centered

## Development Setup

### Prerequisites
- Any modern web browser (Chrome/Edge recommended for PDF export)
- Text editor for JSON/HTML editing
- No package managers, compilers, or build tools required

### Workflow
1. Edit `resume.json` or the embedded `resumeData` object in `resume-renderer.html`
2. Open/refresh `resume-renderer.html` in a browser
3. For PDF: Ctrl/Cmd+P → Save as PDF (recommended margins: 0.5" all sides)

### File Sync Caveat
The renderer currently embeds its own copy of resume data. Changes to `resume.json` do not automatically propagate to the renderer. Manual sync is required until a future enhancement loads the external JSON file.

## Technical Constraints
1. **No server required**: Everything runs client-side in the browser
2. **No external CDN or API calls**: Works fully offline
3. **Browser Print-to-PDF**: PDF generation relies on the browser's built-in print functionality — no programmatic PDF library
4. **Single HTML file**: All CSS and JS are inline; no separate stylesheet or script files
5. **Data duplication**: Resume data exists in both `resume.json` and embedded in `resume-renderer.html`

## Browser Compatibility
| Browser | Status | Notes |
|---------|--------|-------|
| Chrome/Edge | ✅ Recommended | Best PDF export quality |
| Firefox | ✅ Supported | Full rendering support |
| Safari | ✅ Supported | Full rendering support |

## JSON Schema Key Fields

### Experience Entry
```json
{
  "title": "string",
  "company": "string",
  "location": "string",
  "startDate": "YYYY-MM",
  "endDate": "YYYY-MM | null",
  "current": "boolean",
  "highlights": ["string[]"],
  "technologies": ["string[]"]
}
```

### Education Entry
```json
{
  "institution": "string",
  "degree": "string",
  "field": "string",
  "honors": "string | null",
  "graduationDate": "YYYY-MM | null",
  "gpa": "number | null",
  "courses": ["string[] (optional)"]
}
```

### Certification Entry
```json
{
  "name": "string",
  "abbreviation": "string",
  "issuer": "string",
  "date": "YYYY-MM | null",
  "expirationDate": "YYYY-MM | null"
}
```

## Dependencies
**None.** This project has zero external dependencies. No npm packages, no CDN links, no build pipeline.
