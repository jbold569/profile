---
description: Resume writing standards derived from Harvard FAS Career Services and Stack Overflow hiring manager guidance. Rules are labeled by target (CONTENT, STRUCTURE, SCHEMA) to direct AI agents to the correct system component.
author: Jason Bolden
version: 1.0
tags: ["resume", "writing-standards", "content-rules", "structure-rules", "schema-rules"]
globs: ["resume.json", "resume-renderer.html"]
sources:
  - "https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/"
  - "https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/"
  - "https://careerservices.fas.harvard.edu/ai-resumes-and-cover-letters/"
---

# Resume Writing Standards

## Purpose

This document codifies resume writing standards for AI agents editing or generating content within this resume system. Standards are derived from two authoritative sources — Harvard FAS Mignone Center for Career Services and Gergely Orosz (hiring manager, author of *The Tech Resume Inside Out*) — and adapted for a senior cybersecurity/technology leadership context.

**Cross-reference:** These rules complement the global `writing-at-amazon.md` standards. Where overlap exists (active voice, conciseness, data-driven language), Amazon writing standards reinforce these resume-specific rules.

## When This Rule Applies

This rule applies when:
- Editing or generating text content in `resume.json` or the embedded `resumeData` object in `resume-renderer.html`
- Modifying the rendering logic, CSS, or section ordering in `resume-renderer.html`
- Proposing changes to the JSON schema structure
- Reviewing resume content for quality or tailoring for a specific role

---

## Labeling Taxonomy

Every rule in this document carries one of three labels. **AI agents MUST check the label before making changes** to ensure edits target the correct file and component.

| Label | Target File | What It Influences | When to Apply |
|---|---|---|---|
| **📝 CONTENT** | `resume.json` data values | Text strings: `profile`, `highlights[]`, `knowledgeDomains[]`, certification `name` fields | Editing resume text, improving bullet points, tailoring for a role |
| **🏗️ STRUCTURE** | `resume-renderer.html` | CSS styles, section rendering order, visual layout, JavaScript rendering logic | Changing how the resume looks, reordering sections, adjusting formatting |
| **📐 SCHEMA** | `resume.json` field structure | Adding/removing/populating JSON fields, array composition, data types | Adding new data fields, populating empty arrays, schema evolution |

### File Sync Warning
> `resume.json` and the embedded `resumeData` object in `resume-renderer.html` are currently separate copies. Changes to one MUST be reflected in the other. When applying CONTENT or SCHEMA rules, update both files.

---

## Core Philosophy

### The Resume's Single Goal
> **"The goal of your resume is to sell you enough to get a recruiter phone call."** — Gergely Orosz

A resume is not a career autobiography. It is a marketing document. Every line must earn its place by demonstrating fit for the target role.

### The Two-Pass Reading Model

Recruiters and hiring managers read resumes in two passes:

1. **Quick scan (5-10 seconds):** Location, years of experience, technologies, company names, position titles. If the scan fails to match, there is no second read.
2. **Second read (30-60 seconds):** Top-to-bottom reading of content — profile, highlights, skills. This is where bullet quality and quantification matter.

**Implication:** Key information must be immediately scannable. Detailed accomplishments must reward the second read with specifics.

### The Master Resume Strategy
> 📝 CONTENT

Maintain this JSON resume as a comprehensive "master" document. When tailoring for a specific role:
- Reorder highlights within each experience to surface the most relevant first
- Adjust the profile statement to match the target role's language
- Emphasize matching technologies and knowledge domains
- Reduce detail on less relevant earlier positions

---

## 📝 CONTENT Standards

### Profile Statement Rules
> 📝 CONTENT — Applies to: `resume.json → profile` string

The profile statement is the first text a recruiter reads after the header scan. For senior professionals, recruiters pay close attention to this section.

**MUST:**
- Open with your identity and scope: title-level descriptor + years + scale
- Include 2-3 quantified proof points (team size, budget, company scale)
- State the value proposition: what the company gets by hiring you
- Tailor to the target role — adjust emphasis per application

**MUST NOT:**
- Use first-person pronouns ("I", "my", "me")
- Use objective statements ("Seeking a position where...")
- Include generic adjectives without evidence ("innovative", "passionate", "dynamic")
- Exceed 3-4 sentences

**Formula:**
```
[Role descriptor] with [X+ years] [doing what] at [scale/context].
[Proof point with quantification]. [Second proof point].
[Value proposition — what you deliver].
```

**Example (current profile — needs improvement):**
```
❌ "Seeking Senior and Director level leadership roles in cybersecurity or 
risk management that will provide opportunities to lead teams in career 
growth and enhance cybersecurity and risk management capabilities."
```
This sentence is an objective statement focused on what the candidate wants, not what value they bring.

**Improved:**
```
✅ "Delivers measurable security posture improvements through data-driven 
program modernization — including a 92% increase in logging coverage and 
$1.3M annual savings from SIEM migration at American Airlines."
```

### Bullet Writing Formula
> 📝 CONTENT — Applies to: `resume.json → experience[].highlights[]` strings

Every bullet point MUST follow the **Action + Context + Impact** formula:

```
[Strong Action Verb] + [What you did, with scope/scale] + [Measurable result or business impact]
```

For senior leadership roles, extend to four elements:

```
[Action Verb] + [What you did] + [Scale/Scope] + [Business Impact]
```

#### ✅ Strong Bullets (from current resume)
```
"Led strategy and implementation for the migration to next-gen cloud hosted 
SIEM resulting in a 92% increase in logging coverage, $1.3 million in 
savings annually, enhanced behavior-based analytics via AI, and expanded 
use cases into fraud and insider threat"
```
Why it works: Strong verb ("Led"), clear action (migration), quantified results (92%, $1.3M), business context (fraud, insider threat).

```
"Designed a Fraud Investigation System that replaced an existing tool to 
recover $9 million in annual revenue"
```
Why it works: Specific action ("Designed"), concrete deliverable ("Fraud Investigation System"), dollar impact ($9M).

#### ❌ Weak Bullets (from current resume, with fixes)

**Missing quantification:**
```
❌ "Led a team of incident responders responsible for the triage and 
remediation of security issues impacting AWS services and customers 
from cybersecurity threats"

✅ "Led a 12-person incident response team triaging 200+ security events 
monthly, reducing mean time to remediation by 35% for threats impacting 
AWS services and customers"
```

**Vague scope + no impact:**
```
❌ "Worked closely with other departments across the enterprise as a data 
liaison to understand their business needs and mold our Big Data platform 
to meet them"

✅ "Partnered with 8 enterprise departments as data liaison, translating 
business requirements into Big Data platform capabilities that increased 
analytics adoption by 40%"
```

**Passive construction:**
```
❌ "Participated in the development of purple team exercises with partner 
security teams across the organization"

✅ "Co-developed purple team exercises with 4 partner security teams, 
validating detection coverage for 15 MITRE ATT&CK techniques and 
identifying 3 critical gaps in response playbooks"
```

### Language Standards
> 📝 CONTENT — Applies to: all text strings in `resume.json`

#### Active Voice (MUST)
Every bullet MUST use active voice. The subject performs the action.

**Test:** If you can add "by zombies" after the verb and the sentence makes grammatical sense, it is passive voice. Rewrite it.

- ✅ "Reduced phishing incidents by 80%" (active)
- ❌ "Phishing incidents were reduced by 80%" (passive)

#### No Personal Pronouns (MUST)
Resume text MUST NOT contain: I, my, me, we, our, us.

- ✅ "Led hiring for the Seattle site"
- ❌ "Led hiring for my Seattle site" (current resume uses "my" in one bullet)

#### No Unexpanded Abbreviations (MUST)
Spell out abbreviations on first use within each experience entry. The renderer may be parsed by ATS systems or read by non-technical recruiters.

- ✅ "Endpoint Detection and Response (EDR)" on first use, then "EDR"
- ❌ "EDR/EPP" without context

**Exception:** Industry-standard certifications (GIAC, SANS, CISSP) and universally recognized terms (AWS, SQL) may appear without expansion.

#### Quantification Rules (MUST)

Every experience entry SHOULD contain at least 2 quantified bullets. Quantification types:

| Type | Examples |
|---|---|
| **Dollar amounts** | "$7 million portfolio", "$1.3M in savings" |
| **Percentages** | "92% increase", "80% reduction", "98% coverage" |
| **Counts** | "12-person team", "70k endpoints", "500 data points" |
| **Time** | "over the course of 1 month", "in 2 months" |
| **Scale** | "across 3 time zones", "8 enterprise departments" |

**NEVER** use vague quantifiers without data:
- ❌ "significant", "various", "multiple", "several", "numerous"
- ✅ Replace with actual numbers or remove the qualifier

#### Verb Variety (MUST)
No two consecutive bullets within the same experience entry should start with the same verb. Vary across categories (see Action Verb Reference below).

**Current resume issue:** "Led" appears as the opening verb in 5+ bullets across positions. "Managed" appears 4+ times. Diversify using the verb bank.

### Certification Content Rules
> 📝 CONTENT — Applies to: `resume.json → skills.certifications[]`

- `name` field MUST contain the full official certification name
- `abbreviation` field MUST contain the standard abbreviation
- `issuer` field MUST identify the certifying body
- Credly `url` field enables verification — MUST be included when available

---

## 🏗️ STRUCTURE Standards

### Section Ordering
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → `renderResume()` function

For a **senior professional with 10+ years of experience**, the optimal section order is:

1. **Header** (name, contact, LinkedIn, GitHub)
2. **Professional Profile** (executive summary — first thing after scan)
3. **Skills** (certifications, knowledge domains, technical skills — scannable proof)
4. **Experience** (reverse chronological — most recent first)
5. **Education** (brief — degree and institution only for senior professionals)

The current renderer follows this order. **Do not move Education above Experience** for this resume's experience level.

**Source:** Orosz recommends that with extensive experience, education becomes "a brief mention at the end" and a summary section rises to the top.

### Visual Hierarchy & Scannability
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → CSS styles

**MUST maintain:**
- Single-column layout for easy top-to-bottom reading
- Dates, position name, and company name visually separated
- Section headers (`h2`) in uppercase with letter-spacing for quick scanning
- Consistent bullet point styling throughout
- Adequate white space between sections and between job entries

**Current implementation is compliant.** Key CSS values to preserve:
- `h2` with `text-transform: uppercase` and `letter-spacing: 1px`
- `.job-header` separating title, company, and date on distinct lines
- `.contact-info` using flexbox with wrapping

### Skills Presentation Strategy
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → skills rendering logic

Three approaches to presenting technologies (from Orosz), in order of preference:

1. **Inline weaving (PREFERRED):** Mention technologies within experience highlight bullets. Provides context on when and how each tool was used.
2. **Separate section:** List technologies in a dedicated Skills section. Good for quick scanning.
3. **Per-position callout:** List technologies at the end of each experience entry using the `technologies[]` array.

**Recommendation:** Use a hybrid approach:
- Weave key technologies into highlight bullets (CONTENT rule)
- Render the `technical` skills grid in the Skills section when arrays are populated (STRUCTURE rule)
- Render `technologies[]` tags at the bottom of each experience entry (STRUCTURE rule — not yet implemented)

### Contact Information Privacy
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → header rendering

**MUST render:** City, State (not full street address), phone, email, LinkedIn, GitHub
**MUST NOT render:** Full street address in the visual output (it exists in the JSON for records)

The current renderer correctly shows only city/state. Preserve this behavior.

### Date Formatting
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → `formatDate()` function

- Dates MUST render as `Mon YYYY` format (e.g., "Nov 2022")
- Current positions MUST show "Present" as the end date
- Date ranges MUST use an en dash: "Nov 2022 – Present"
- Dates MUST be consistently scannable in a top-to-bottom visual line

### Print Optimization
> 🏗️ STRUCTURE — Applies to: `resume-renderer.html` → `@media print` CSS

- Job entries (`page-break-inside: avoid`) — prevent splitting a job across pages
- Sections (`page-break-inside: avoid`) — keep section headers with their content
- Remove background colors and box shadows for clean printing
- Reduce padding for print to maximize content density

---

## 📐 SCHEMA Standards

### Required Field Population
> 📐 SCHEMA — Applies to: `resume.json` field completeness

The following fields are currently empty and MUST be populated:

| Field Path | Status | Priority |
|---|---|---|
| `skills.technical.platforms[]` | Empty | **HIGH** — Add: AWS, Azure, GCP, etc. |
| `skills.technical.tools[]` | Empty | **HIGH** — Add: CrowdStrike, Splunk, SOAR platforms, etc. |
| `skills.technical.languages[]` | Empty | **MEDIUM** — Add: Python, SQL, KQL, etc. |
| `skills.technical.frameworks[]` | Empty | **MEDIUM** — Add: MITRE ATT&CK, NIST CSF, Kill Chain, etc. |
| `skills.certifications[].date` | All null | **MEDIUM** — Add issuance dates |
| `skills.certifications[].expirationDate` | All null | **MEDIUM** — Add expiration dates |
| `experience[].location` | Most empty | **LOW** — Add city/state for each position |

### Technologies Array Completeness
> 📐 SCHEMA — Applies to: `resume.json → experience[].technologies[]`

Every experience entry SHOULD have its `technologies[]` array populated with the key tools and platforms used in that role. Currently only 2 of 5 positions have populated arrays.

| Position | Current `technologies[]` | Should Add |
|---|---|---|
| AWS CloudSec | `[]` | AWS services, internal IR tools, cloud-native security |
| Cruise CIRT | `[]` | SOAR platforms evaluated, SIEM, EDR |
| AA CIRE | `["CrowdStrike", "SIEM", "SOAR", "TIP"]` | Specific SIEM name, specific SOAR name, EDR/EPP |
| AA SAE | `[]` | Log management stack, Splunk/ELK, cloud platforms |
| AA Data Analytics | `["Cloudera", "Big Data"]` | Specific Cloudera tools (Impala, Hive, HDFS, etc.) |

### Schema Extension Recommendations
> 📐 SCHEMA — Applies to: `resume.json` structural additions

**SHOULD consider adding:**

1. **`experience[].summary`** — A one-line summary per position for use in condensed/tailored views
2. **`experience[].keywords[]`** — ATS-optimized keywords per position, distinct from technologies
3. **`profile_variants`** — Object containing alternate profile statements keyed by target role type (e.g., "director_security_ops", "ciso_advisory", "senior_manager_ir")
4. **`metadata.lastUpdated`** — ISO date string tracking when content was last reviewed
5. **`metadata.targetRoles[]`** — Array of role types this resume is optimized for

---

## AI-Assisted Editing Guidelines

> Based on Harvard FAS "AI for Resumes and Cover Letters" guidance

### Principles for AI Agents Editing This Resume

1. **Start from existing content.** Work with the human-authored highlights and profile. Improve precision, quantification, and verb choice — do not rewrite from scratch.

2. **Preserve authenticity.** Every bullet must represent actual accomplishments the candidate can speak to in an interview. Do not fabricate metrics or inflate scope.

3. **Edit bullet-by-bullet.** Process each highlight individually for precise improvements rather than batch-rewriting entire experience sections.

4. **Tailor to audience.** When a target role is specified, adjust emphasis and keyword density to match the job description. Use the master resume approach — reorder and adjust, don't fabricate.

5. **Optimize for scannability.** Ensure key technologies, metrics, and scope indicators appear early in each bullet (within the first 10-15 words) where possible.

6. **Flag gaps transparently.** If a bullet lacks quantification and the AI cannot reasonably infer a metric, flag it for human input rather than inventing a number.

### AI Editing Prompts (Adapted from Harvard)

When using AI tools to improve resume content, these prompt patterns are effective:

- **REVISE:** "Based on this job description [insert], generate 5 suggestions for improving this bullet point: [insert bullet]"
- **ACTION VERBS:** "Suggest 5 alternative action verbs for this cybersecurity leadership bullet: [insert bullet]"
- **SKILL MATCH:** "Compare this resume section [insert] against this job description [insert] and identify gaps in keyword coverage"
- **ROLE PLAY:** "As a recruiter for [company/role], provide feedback on this experience section. Identify strengths and gaps."

---

## Self-Editing Checklist

Before finalizing any resume content changes, verify against this checklist:

### Content Quality
- [ ] Every bullet starts with a strong, varied action verb
- [ ] No two consecutive bullets in the same entry start with the same verb
- [ ] At least 2 bullets per experience entry contain quantified results
- [ ] Profile statement contains no first-person pronouns
- [ ] Profile statement leads with value proposition, not objective
- [ ] No vague quantifiers ("significant", "various", "multiple") without data
- [ ] All abbreviations expanded on first use within each entry
- [ ] Technologies mentioned in bullets match the `technologies[]` array

### Structural Quality
- [ ] Section order follows senior-professional convention (Profile → Skills → Experience → Education)
- [ ] Dates scan cleanly in a vertical line
- [ ] Company name, title, and date are visually separated
- [ ] White space is balanced between sections
- [ ] Print view renders cleanly without split job entries

### Schema Completeness
- [ ] `technical.platforms[]` populated
- [ ] `technical.tools[]` populated
- [ ] All `experience[].technologies[]` arrays populated
- [ ] All certification dates populated
- [ ] `resume.json` and embedded `resumeData` are in sync

### Data Consistency
- [ ] Numbers use numerals (not words): "12 teams" not "twelve teams"
- [ ] Dollar amounts use consistent format: "$1.3 million" or "$1.3M"
- [ ] Dates use consistent YYYY-MM format in JSON, Mon YYYY in rendered view
- [ ] No spelling or grammatical errors

---

## Anti-Patterns

### ❌ CONTENT Anti-Patterns
| Anti-Pattern | Example | Fix |
|---|---|---|
| **Duty description, not accomplishment** | "Responsible for managing vendor relationships" | "Orchestrated 3 vendor partnerships, improving SLA compliance by 25%" |
| **Passive construction** | "Phishing incidents were reduced by 80%" | "Reduced phishing incidents by 80% by upgrading email protection gateway" |
| **Personal pronouns** | "Managed career progression of 60% of my staff" | "Managed career progression of 60% of direct reports" |
| **Vague scope** | "Worked with various teams" | "Partnered with 8 cross-functional teams" |
| **Repeated verbs** | Led... Led... Led... Led... | Led... Orchestrated... Spearheaded... Drove... |
| **No impact stated** | "Developed training program" | "Developed training program for 25 staff, reducing onboarding time by 40%" |
| **Objective statement in profile** | "Seeking opportunities to lead..." | "Delivers measurable security improvements through..." |
| **Generic adjectives** | "innovative leader", "passionate about security" | Remove or replace with evidence |

### ❌ STRUCTURE Anti-Patterns
| Anti-Pattern | Fix |
|---|---|
| Multi-column layout that breaks scanning | Single-column, top-to-bottom reading |
| Education listed before Experience (for senior roles) | Move Education to bottom |
| Inconsistent date formatting | Enforce Mon YYYY throughout |
| Full street address visible in rendered resume | Show only City, State |
| Cramped text with no white space | Maintain spacing between sections and entries |

### ❌ SCHEMA Anti-Patterns
| Anti-Pattern | Fix |
|---|---|
| Empty `technologies[]` arrays | Populate for every position |
| Missing certification dates | Add `date` and `expirationDate` |
| Data divergence between `resume.json` and embedded `resumeData` | Sync after every edit |
| Inconsistent date format strings | Use `YYYY-MM` for all dates |

---

## Action Verb Reference Bank

Organized by category. For cybersecurity and technology leadership resumes, prioritize verbs from **Leadership**, **Technical**, **Quantitative**, and **Organizational** categories.

### Leadership
Accomplished · Achieved · Administered · Analyzed · Assigned · Attained · Chaired · Consolidated · Contracted · Coordinated · Delegated · Developed · Directed · Earned · Evaluated · Executed · Handled · Headed · Impacted · Improved · Increased · Led · Mastered · Orchestrated · Organized · Oversaw · Planned · Predicted · Prioritized · Produced · Proved · Recommended · Regulated · Reorganized · Reviewed · Scheduled · Spearheaded · Strengthened · Supervised · Surpassed

### Communication
Addressed · Arbitrated · Arranged · Authored · Collaborated · Convinced · Corresponded · Delivered · Developed · Directed · Documented · Drafted · Edited · Energized · Enlisted · Formulated · Influenced · Interpreted · Lectured · Liaised · Mediated · Moderated · Negotiated · Persuaded · Presented · Promoted · Publicized · Reconciled · Recruited · Reported · Rewrote · Spoke · Suggested · Synthesized · Translated · Verbalized · Wrote

### Research
Clarified · Collected · Concluded · Conducted · Constructed · Critiqued · Derived · Determined · Diagnosed · Discovered · Evaluated · Examined · Extracted · Formed · Identified · Inspected · Interpreted · Interviewed · Investigated · Modeled · Organized · Resolved · Reviewed · Summarized · Surveyed · Systematized · Tested

### Technical
Assembled · Built · Calculated · Computed · Designed · Devised · Engineered · Fabricated · Installed · Maintained · Operated · Optimized · Overhauled · Programmed · Remodeled · Repaired · Solved · Standardized · Streamlined · Upgraded

### Teaching & Mentoring
Adapted · Advised · Clarified · Coached · Communicated · Coordinated · Demystified · Developed · Enabled · Encouraged · Evaluated · Explained · Facilitated · Guided · Informed · Instructed · Persuaded · Set Goals · Stimulated · Studied · Taught · Trained

### Quantitative & Financial
Administered · Allocated · Analyzed · Appraised · Audited · Balanced · Budgeted · Calculated · Computed · Developed · Forecasted · Managed · Marketed · Maximized · Minimized · Planned · Projected · Researched

### Creative & Strategic
Acted · Composed · Conceived · Conceptualized · Created · Customized · Designed · Developed · Directed · Established · Fashioned · Founded · Illustrated · Initiated · Instituted · Integrated · Introduced · Invented · Originated · Performed · Planned · Published · Redesigned · Revised · Revitalized · Shaped · Visualized

### Helping & Supporting
Assessed · Assisted · Clarified · Coached · Counseled · Demonstrated · Diagnosed · Educated · Enhanced · Expedited · Facilitated · Familiarized · Guided · Motivated · Participated · Proposed · Provided · Referred · Rehabilitated · Represented · Served · Supported

### Organizational & Operational
Approved · Accelerated · Added · Arranged · Broadened · Cataloged · Centralized · Changed · Classified · Collected · Compiled · Completed · Controlled · Defined · Dispatched · Executed · Expanded · Gained · Gathered · Generated · Implemented · Inspected · Launched · Monitored · Operated · Organized · Prepared · Processed · Purchased · Recorded · Reduced · Reinforced · Retrieved · Screened · Selected · Simplified · Sold · Specified · Steered · Structured · Systematized · Tabulated · Unified · Updated · Utilized · Validated · Verified

---

## Source Attribution

This document synthesizes resume writing standards from the following authoritative sources:

1. **Harvard FAS Mignone Center for Career Services** — "Create a Strong Resume"
   - URL: https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/
   - Content: Resume tips, action verbs, DO/DON'T lists, formatting standards
   - Sample PDFs: resume-sample.pdf, category-sample.pdf (annotated examples)
   - Last accessed: March 25, 2026

2. **Harvard FAS — "AI for Resumes and Cover Letters"**
   - URL: https://careerservices.fas.harvard.edu/ai-resumes-and-cover-letters/
   - Content: AI-assisted editing principles, ATS optimization, example prompts
   - Last accessed: March 25, 2026

3. **Stack Overflow Blog — Gergely Orosz** — "How to write an effective developer resume: Advice from a hiring manager"
   - URL: https://stackoverflow.blog/2020/11/25/how-to-write-an-effective-developer-resume-advice-from-a-hiring-manager/
   - Content: 7 core resume principles from reviewing hundreds of resumes and interviewing recruiters at Google, Facebook, Microsoft
   - Book reference: *The Tech Resume Inside Out* (https://thetechresume.com/)
   - Last accessed: March 25, 2026

4. **Harvard FAS Resume Templates**
   - Bullet point template: https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/
   - Paragraph template: https://careerservices.fas.harvard.edu/resources/harvard-college-paragraph-resume-template/
   - Available in Word (.docx) and Google Docs formats

---

*Standards compiled March 25, 2026. Review and update when sources publish new guidance or resume system schema changes.*
