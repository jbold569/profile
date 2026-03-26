# Project Brief

## Overview
A maintainable resume system using JSON for structured content and HTML/CSS/JavaScript for rendering, replacing an outdated Word document format.

## Owner
**Jason Bolden** — Cybersecurity leader with 12+ years of experience in security operations and incident response. Currently Manager – Cloud Response at Amazon Web Services.

## Core Requirements
1. **Structured Data**: Resume content stored in JSON with a well-defined schema for easy editing and version control
2. **Professional Rendering**: Clean, modern HTML/CSS presentation suitable for senior/director-level leadership roles
3. **PDF Export**: Print-optimized output via browser Print-to-PDF workflow
4. **Self-Contained**: No external dependencies — pure HTML/CSS/JS, works offline
5. **Maintainability**: Update content by editing JSON without touching presentation logic

## Target Audience
Hiring managers and recruiters for **Senior and Director level leadership roles** in cybersecurity and risk management.

## Key Design Decisions
- **Combined Profile Section**: Professional summary + objective in a single paragraph (value proposition first, career goals second)
- **Certifications in Skills**: Kept under skills rather than education per user preference
- **Metrics in Highlights**: Quantitative achievements embedded in bullet points for natural reading
- **No Clearances/Awards Sections**: Not applicable; can be added later if needed
- **ISO Date Format**: `YYYY-MM` in JSON for sorting and consistency

## Success Criteria
- Resume renders cleanly in all modern browsers
- PDF output is professional and suitable for leadership-level applications
- Content updates require only JSON edits
- System is portable and works without internet connectivity
