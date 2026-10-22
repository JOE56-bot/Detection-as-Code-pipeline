# 🔐 Detection-as-Code Pipeline

### Automated Security Detection Development, Validation & Testing

![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)
![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-critical)
![Sigma](https://img.shields.io/badge/Sigma-Rules-orange)
![KQL](https://img.shields.io/badge/KQL-Microsoft%20Security-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)
![PowerShell](https://img.shields.io/badge/PowerShell-Detection%20Telemetry-5391FE?logo=powershell&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Configuration-lightgrey)

---

## 📖 Project Overview

The **Detection-as-Code Pipeline** is a cybersecurity engineering project focused on developing, version-controlling, validating, testing, and documenting security detections as code.

The project applies software engineering principles to detection engineering by treating detection rules as maintainable code rather than manually managed SIEM configurations.

The pipeline is designed around:

- **Sigma** detection rules
- **Kusto Query Language (KQL)**
- **Git & GitHub**
- **GitHub Actions**
- **Automated validation**
- **Detection testing**
- **MITRE ATT&CK mapping**
- **Version-controlled detection development**

The project builds upon practical endpoint detection work from the **Windows Attack Telemetry Research Lab** and is designed to demonstrate a repeatable Detection Engineering workflow.

---

## 🎯 Objectives

- Develop reusable Sigma detection rules.
- Develop corresponding KQL detections.
- Store detections in version control.
- Automatically validate detection syntax.
- Implement automated detection testing.
- Use GitHub Actions for continuous validation.
- Map detections to MITRE ATT&CK.
- Document detection logic and expected behavior.
- Track detection changes through Git history.
- Establish a foundation for future automated deployment.

---

## 🏗️ Detection-as-Code Architecture

```text
                    Security Telemetry
                           │
                           ▼
                  Detection Development
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        Sigma Detection             KQL Detection
              │                         │
              └────────────┬────────────┘
                           ▼
                    Git Repository
                           │
                           ▼
                    GitHub Actions
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Syntax Validation          Detection Tests
              │                         │
              └────────────┬────────────┘
                           ▼
                   Validation Results
                           │
                           ▼
                 MITRE ATT&CK Mapping
                           │
                           ▼
                  Detection Repository
```

---

## 🔄 Detection Engineering Workflow

```text
1. Identify Threat
       ↓
2. Develop Detection
       ↓
3. Write Sigma Rule
       ↓
4. Develop KQL Query
       ↓
5. Validate Syntax
       ↓
6. Test Detection
       ↓
7. Map to MITRE ATT&CK
       ↓
8. Commit to Git
       ↓
9. GitHub Actions Validation
       ↓
10. Review & Improve
```

---

## 📂 Repository Structure

```text
Detection-as-Code-Pipeline/
│
├── detections/
│   ├── sigma/
│   └── kql/
│
├── tests/
│   ├── sigma/
│   └── kql/
│
├── scripts/
│
├── .github/
│   └── workflows/
│
├── docs/
│   ├── architecture/
│   └── detection-development/
│
├── screenshots/
│
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
└── ROADMAP.md
```

---

## 🧪 Detection Testing

The project will progressively introduce automated testing for detections.

Testing will focus on:

- Valid detection syntax
- Required metadata
- Detection logic
- Expected positive matches
- Expected negative matches
- False-positive considerations
- MITRE ATT&CK mappings

Example testing concept:

```text
Detection Rule
      │
      ├── Malicious Test Case → SHOULD MATCH
      │
      └── Benign Test Case    → SHOULD NOT MATCH
```

---

## 🧩 Sigma Detection Engineering

Sigma rules provide a vendor-neutral format for representing security detections.

Example detection workflow:

```text
Sigma Rule
    │
    ├── Detection Logic
    ├── Metadata
    ├── Severity
    ├── Tags
    └── MITRE ATT&CK
            │
            ▼
       Validation
            │
            ▼
       Conversion
            │
            ▼
        KQL / SIEM
```

---

## 🔎 KQL Detection Library

KQL detections will provide Microsoft-focused implementations of the detection logic.

Planned detections include:

| Detection | Technology | Status |
|---|---|:---:|
| Encoded PowerShell | Sigma + KQL | 🚧 |
| Suspicious PowerShell | Sigma + KQL | ⬜ |
| Account Discovery | Sigma + KQL | ⬜ |
| System Information Discovery | Sigma + KQL | ⬜ |
| Network Configuration Discovery | Sigma + KQL | ⬜ |

---

## ⚙️ GitHub Actions

GitHub Actions will provide continuous validation whenever detection code is changed.

Planned workflow:

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
Pull Request / Push
    │
    ▼
GitHub Actions
    │
    ├── Validate Sigma
    │
    ├── Validate Metadata
    │
    ├── Run Detection Tests
    │
    └── Generate Results
             │
             ▼
        Pass / Fail
```

---

## 🎯 MITRE ATT&CK Mapping

Each detection will be mapped to relevant MITRE ATT&CK techniques.

Initial coverage will build from techniques investigated in the Windows Attack Telemetry Research Lab.

| Technique | Description | Detection Status |
|---|---|:---:|
| T1059.001 | PowerShell | 🚧 |
| T1087 | Account Discovery | 🚧 |
| T1082 | System Information Discovery | 🚧 |
| T1016 | System Network Configuration Discovery | 🚧 |

---

## 🛡️ Detection Development Standards

Each detection should include:

- Unique detection name
- Description
- Author
- Date
- Log source
- Detection logic
- Severity
- MITRE ATT&CK mapping
- False positives
- Investigation guidance
- References
- Testing information

This creates consistent and maintainable detection content.

---

## 📊 Detection Lifecycle

```text
        ┌───────────────┐
        │ Threat Intel  │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │ Detection Dev │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │    Testing    │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │   Validation  │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │   Deployment  │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │   Monitoring  │
        └───────┬───────┘
                ↓
        ┌───────────────┐
        │ Improvement   │
        └───────┬───────┘
                │
                └──────────────→ Detection Development
```

---

## 🛣️ Roadmap

### Phase 1 — Repository Foundation

- [x] Create GitHub repository
- [ ] Create repository structure
- [ ] Add README
- [ ] Add project documentation
- [ ] Establish detection naming standards

### Phase 2 — Sigma Validation

- [ ] Add Sigma rules
- [ ] Install Sigma tooling
- [ ] Validate Sigma syntax
- [ ] Implement automated validation

### Phase 3 — KQL Detection Library

- [ ] Add KQL detections
- [ ] Document data sources
- [ ] Standardize query structure
- [ ] Add detection metadata

### Phase 4 — Detection Testing

- [ ] Create positive test cases
- [ ] Create negative test cases
- [ ] Validate detection behavior
- [ ] Document test results

### Phase 5 — CI/CD

- [ ] Create GitHub Actions workflow
- [ ] Automate Sigma validation
- [ ] Automate detection testing
- [ ] Generate validation reports
- [ ] Implement pull-request checks

### Phase 6 — MITRE ATT&CK

- [ ] Map detections to ATT&CK
- [ ] Track technique coverage
- [ ] Create ATT&CK coverage documentation

### Phase 7 — Advanced Automation

- [ ] Detection deployment workflow
- [ ] Automated conversion
- [ ] Detection quality checks
- [ ] Versioned detection releases

---

## 📚 Related Projects

### 🛡️ Windows Attack Telemetry Research Lab

Endpoint-focused security research involving:

- Windows telemetry
- Sysmon
- PowerShell
- KQL
- Sigma
- Threat Hunting
- MITRE ATT&CK
- Atomic Red Team

### ☁️ Cloud Threat Detection Lab

Cloud-focused Detection Engineering involving:

- Microsoft Azure
- Microsoft Sentinel
- Azure Monitor
- Log Analytics
- Microsoft Entra ID
- KQL
- Cloud Threat Hunting
- MITRE ATT&CK

---

## 💻 Technologies

**Detection**

`Sigma` `KQL` `MITRE ATT&CK`

**Automation**

`GitHub Actions` `PowerShell`

**Version Control**

`Git` `GitHub`

**Security**

`Threat Hunting` `Detection Engineering` `SIEM`

---

## ⚠️ Disclaimer

This project is developed for educational and defensive cybersecurity purposes in authorized lab environments.

All attack simulations and detection testing are performed only against systems and environments where the author has explicit authorization.

---

## 👨‍💻 Author

**Jose van Schalkwyk**

Aspiring Detection Engineer | Threat Hunter | Purple Team Practitioner

---

⭐ **This repository demonstrates the development of security detections using software engineering, automation, testing, and version control principles.**
