# 🔐 Detection-as-Code Pipeline

### Automated Security Detection Development, Validation & Testing

![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)
![Detection Engineering](https://img.shields.io/badge/Detection-Engineering-critical)
![Sigma](https://img.shields.io/badge/Sigma-Rules-orange)
![KQL](https://img.shields.io/badge/KQL-Microsoft%20Security-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF?logo=githubactions&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red)

---

## 📖 Project Overview

The **Detection-as-Code Pipeline** is a cybersecurity engineering project focused on developing, version-controlling, validating, testing, and documenting security detections as code.

It applies software engineering principles to detection engineering by treating detection rules as maintainable, version-controlled artifacts rather than manually managed SIEM configurations.

The project uses Sigma, Git, GitHub, and GitHub Actions to establish a repeatable detection development and validation workflow.

The initial implementation focuses on automated Sigma rule validation, with future expansion planned for KQL detections, automated testing, and detection deployment.

## 🎯 Project Objectives

- Develop reusable Sigma detection rules.
- Establish consistent detection metadata standards.
- Store detection content in Git version control.
- Automatically validate Sigma rules.
- Reject detection rules containing validation issues.
- Use GitHub Actions for continuous integration.
- Review detection changes through pull requests.
- Map detections to MITRE ATT&CK.
- Build a foundation for future detection testing and deployment.

## 🏗️ Architecture

```text
       Security Telemetry
              |
              v
      Detection Development
              |
              v
       Sigma Detection Rules
              |
              v
        Git Repository
              |
              v
       GitHub Actions CI
              |
              v
      Sigma CLI Validation
              |
        +-----+-----+
        |           |
        v           v
      PASS         FAIL
        |           |
        v           v
   Validation    Review and
    Successful   Correction
        |
        v
    Pull Request
        |
        v
     Code Review
        |
        v
   Merge to Main
```

## 🔄 Implemented Workflow

1. Develop a Sigma detection rule.
2. Store the rule in the repository.
3. Validate the rule locally using Sigma CLI.
4. Commit and push changes to GitHub.
5. Trigger GitHub Actions validation.
6. Reject rules containing validation issues.
7. Review changes through a pull request.
8. Merge approved changes into the main branch.

## 📂 Repository Structure

```text
Detection-as-Code-Pipeline/
│
├── .github/
│   └── workflows/
│       └── sigma-validation.yml
│
├── detections/
│   ├── sigma/
│   │   └── encoded-powershell.yml
│   └── kql/
│
├── tests/
│   ├── sigma/
│   └── kql/
│
├── scripts/
│
├── docs/
│   ├── architecture
│   ├── detection-development
│   └── evidence/
│
├── screenshots/
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── ROADMAP.md
└── .gitignore
```

## 🧪 Implemented Sigma Detection

### PowerShell Encoded Command

**File:** `detections/sigma/encoded-powershell.yml`

This detection identifies Windows process creation events where PowerShell is launched with encoded-command parameters.

| Attribute | Value |
|---|---|
| Detection | PowerShell Encoded Command |
| Platform | Windows |
| Category | Process Creation |
| Severity | Medium |
| Status | Experimental |
| MITRE ATT&CK | T1059.001 |
| Technology | Sigma |

The detection searches command-line data for:

- `-enc`
- `-encodedcommand`

**False-positive consideration:** Legitimate administrative scripts and automation workflows may use encoded PowerShell commands.

## ⚙️ Continuous Integration — GitHub Actions

The repository includes an automated GitHub Actions workflow:

`.github/workflows/sigma-validation.yml`

The workflow:

1. Checks out the repository.
2. Configures Python.
3. Installs Sigma CLI.
4. Validates the Sigma detection directory.
5. Fails the validation job if issues are detected.

The strict validation command is:

```bash
sigma check --fail-on-issues detections/sigma/
```

The `--fail-on-issues` option ensures that validation issues are treated as failures rather than silently accepted.

### Validation Results

The pipeline has been tested with both valid and invalid Sigma detection content.

| Test | Expected result | Observed result |
|---|---|---|
| Valid Sigma rule | Pass | Passed |
| Invalid rule missing required identifier | Fail | Failed |
| Corrected detection directory | Pass | Passed |
| GitHub Actions validation | Pass | Passed |

The invalid-rule test demonstrated that the CI pipeline can reject a rule containing a validation issue.

## 🔀 Version Control and Pull Requests

Git and GitHub are used to manage detection development.

The project uses:

- Feature and test branches.
- Version-controlled detection rules.
- Pull request reviews.
- Automated validation checks.
- Controlled merging into `main`.

The initial strict-validation implementation was tested on a separate branch and successfully merged into `main` after all checks passed.

## 🎯 MITRE ATT&CK Mapping

The initial detection maps to:

| Technique | Description | Status |
|---|---|---|
| T1059.001 | PowerShell | Implemented in Sigma rule |
| T1087 | Account Discovery | Planned |
| T1082 | System Information Discovery | Planned |
| T1016 | System Network Configuration Discovery | Planned |

## 🔎 KQL Detection Library

Kusto Query Language detections are planned as a future expansion.

The objective is to develop Microsoft-focused implementations of detection logic and document the associated data sources.

Planned detections include:

- Encoded PowerShell.
- Suspicious PowerShell activity.
- Account Discovery.
- System Information Discovery.
- Network Configuration Discovery.

No KQL detection implementation is claimed as completed in the current milestone.

## 🛡️ Detection Development Standards

Detection rules should include:

- Unique identifier.
- Detection title.
- Description.
- Author.
- Date.
- Log source.
- Detection logic.
- Severity.
- False-positive considerations.
- MITRE ATT&CK tags.

Future detection enhancements will include investigation guidance, references, and positive and negative test cases.

## 🛣️ Project Roadmap

### Phase 1 — Repository Foundation
- [x] Create GitHub repository.
- [x] Establish repository structure.
- [x] Create README and supporting project files.
- [x] Configure Git version control.

### Phase 2 — Sigma Validation
- [x] Install Sigma CLI.
- [x] Develop initial Sigma detection.
- [x] Validate Sigma syntax.
- [x] Implement GitHub Actions validation.
- [x] Enable strict validation.
- [x] Test rejection of invalid Sigma rules.

### Phase 3 — Pull Request Workflow
- [x] Create a test branch.
- [x] Validate detection changes.
- [x] Verify automated CI failure handling.
- [x] Successfully merge validated changes into main.

### Phase 4 — KQL Detection Library
- [ ] Develop KQL detections.
- [ ] Document data sources.
- [ ] Standardize query structure.
- [ ] Add detection metadata.

### Phase 5 — Detection Testing
- [ ] Create positive test cases.
- [ ] Create negative test cases.
- [ ] Test detection behavior against telemetry.
- [ ] Document test results.

### Phase 6 — Advanced Automation
- [ ] Automate Sigma conversion.
- [ ] Introduce additional detection quality checks.
- [ ] Generate validation reports.
- [ ] Develop detection deployment workflows.

## 💻 Technologies

**Detection Engineering**

`Sigma` `KQL` `MITRE ATT&CK`

**Automation**

`GitHub Actions` `Python` `Sigma CLI`

**Version Control**

`Git` `GitHub`

**Security**

`Detection Engineering` `Threat Hunting` `SIEM`

## 📚 Related Projects

### Windows Attack Telemetry Research Lab

Endpoint-focused security research involving Windows telemetry, Sysmon, PowerShell, Sigma, KQL, threat hunting, and MITRE ATT&CK.

### Cloud Threat Detection Lab

Cloud-focused detection engineering involving Microsoft Azure, Microsoft Sentinel, Azure Monitor, Log Analytics, and Microsoft Entra ID.

## ⚠️ Disclaimer

This project is developed for educational and defensive cybersecurity purposes in authorized lab environments.

All attack simulations and detection testing are performed only against systems and environments where the author has explicit authorization.

## 👨‍💻 Author

**Jose van Schalkwyk**

Aspiring Detection Engineer | Threat Hunter | Purple Team Practitioner

---

⭐ This repository demonstrates the application of software engineering, version control, automated validation, and detection engineering principles to security detection development.n
