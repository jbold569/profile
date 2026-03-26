# Product Context

## Why This Project Exists
Jason Bolden's resume was previously maintained as a traditional Word document. This format was difficult to update consistently, offered limited flexibility for creating different versions, and did not support version control. This project replaces that approach with a structured, data-driven resume system.

## Problems It Solves
1. **Maintainability**: Content is separated from presentation — update JSON data without touching HTML/CSS
2. **Consistency**: Structured schema enforces uniform formatting across all sections
3. **Version Control**: JSON and HTML files are Git-friendly, enabling change tracking over time
4. **Flexibility**: The same data can power multiple renderers, themes, or export formats
5. **Portability**: Pure HTML/CSS/JS with zero dependencies — works offline in any modern browser

## How It Works
1. Resume content is authored and maintained in `resume.json` using a well-defined schema
2. The `resume-renderer.html` file reads the JSON data and renders a professional resume in the browser
3. Date formatting (`YYYY-MM` → `Mon YYYY`) and current-role handling (`null` endDate → "Present") are automatic
4. PDF export is achieved via the browser's built-in Print-to-PDF functionality with print-optimized CSS

## User Experience Goals
- **Clean, professional appearance**: Navy blue headers (#2c3e50), light blue accents (#3498db), Segoe UI typography
- **Leadership-appropriate design**: Single-column layout, max-width 850px — suitable for senior/director-level roles
- **Easy content updates**: Edit JSON values, refresh browser, see changes immediately
- **Quality PDF output**: Optimized for letter-size paper with proper margins, no shadows, and prevented page breaks within job entries
- **Responsive viewing**: Adapts to mobile and tablet screens for convenient reviewing on any device

## Target User Profile
- **Name**: Jason Bolden
- **Current Role**: Manager – Cloud Response (CloudSec), Amazon Web Services
- **Career Focus**: Senior and Director level cybersecurity leadership
- **Experience**: 12+ years across AWS, Cruise LLC, and American Airlines
- **Certifications**: 4 GIAC certifications (GSLC, GCIH, GSOM, GSTRT)
- **Education**: B.S. Computer Engineering from Texas A&M University (with Honors)
