# Simulated Web Application Security Assessment (E-commerce Platform)

## Summary
Security assessment of a simulated e-commerce web application to identify weaknesses related to input validation, access to internal resources, and business logic controls. The assessment focused on identifying vulnerabilities that could lead to sensitive data exposure and financial abuse.

## Key Findings
### 1) Server-Side Request Forgery (SSRF) — High
- Identified an SSRF weakness in the checkout / receipt generation workflow where user-controlled SVG content was processed without sufficient restrictions.
- Demonstrated impact by coercing the server to retrieve an internal file and exposing sensitive data.

### 2) Business Logic Abuse / Insufficient Server-Side Validation — Medium
- Identified improper server-side validation of item quantity/amount values during checkout.
- Demonstrated impact by manipulating values resulting in incorrect (negative) order totals, indicating potential financial abuse.

## Skills Demonstrated
- Web application security testing methodology
- HTTP request inspection and manipulation (Burp Suite)
- Risk rating and impact analysis
- Clear reporting and remediation planning

## Tools
- Burp Suite

## Deliverables
- [**Report.pdf**](./Report.pdf) – full write-up with evidence and remediation guidance
- Screenshots (selected supporting evidence)
