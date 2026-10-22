# Detection-as-Code Pipeline

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/YOUR-USERNAME/YOUR-REPOSITORY/validate.yml?label=CI%20Validation\&logo=github)
![Sigma](https://img.shields.io/badge/Sigma-Detection%20Rules-blue)
![KQL](https://img.shields.io/badge/KQL-Threat%20Hunting-purple)
![MITRE ATT%26CK](https://img.shields.io/badge/MITRE%20ATT%26CK-Mapped-red)
![YAML](https://img.shields.io/badge/Rules-YAML-orange)
![Python](https://img.shields.io/badge/Python-3.x-yellow?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

This project implements a **Detection-as-Code (DaC) pipeline** for developing, validating, testing, and maintaining cybersecurity detection rules using version-controlled detection content.

The project is designed to demonstrate practical **detection engineering**, including:

* Sigma rule development
* KQL threat detection and hunting
* MITRE ATT&CK mapping
* Detection rule validation
* Automated CI/CD validation
* Detection testing
* Git-based change management
* Security-focused documentation

The project builds upon telemetry and detection engineering experience developed in a previous Windows endpoint telemetry research lab.

---

## Project Goals

The primary objectives are to build a repeatable and maintainable detection engineering workflow.

### Detection Engineering

* Develop detections from security telemetry
* Write reusable Sigma rules
* Translate detections into KQL
* Map detections to MITRE ATT&CK techniques
* Document detection logic and assumptions

### Automation

* Automatically validate detection rules
* Detect malformed YAML and invalid Sigma syntax
* Run validation whenever detection content changes
* Use GitHub Actions as the CI layer

### Testing

* Create repeatable detection test cases
* Use controlled security simulations
* Compare expected telemetry against detection logic
* Document detection results and limitations

### Portfolio Development

This repository is intended to demonstrate practical skills relevant to:

* SOC Analyst
* Security Operations
* Detection Engineering
* Threat Detection
* Threat Hunting
* Blue Team
* Security Engineering

---

# Architecture

```text
                    ┌──────────────────────┐
                    │   Detection Author   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Git / GitHub    │
                    │   Detection Changes  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   GitHub Actions     │
                    │    CI Validation     │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌─────────────────┐
        │  Sigma Rules    │        │   KQL Queries   │
        │     YAML        │        │   Detection     │
        └────────┬────────┘        └────────┬────────┘
                 │                          │
                 ▼                          ▼
        ┌─────────────────┐        ┌─────────────────┐
        │ Rule Validation │        │ Threat Hunting  │
        └────────┬────────┘        └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Detection Tests │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ MITRE ATT&CK    │
        │    Mapping      │
        └─────────────────┘
```

---

# Repository Structure

```text
detection-as-code/
│
├── .github/
│   └── workflows/
│       └── validate.yml
│
├── detections/
│   ├── sigma/
│   │   ├── windows/
│   │   ├── powershell/
│   │   └── process/
│   │
│   └── kql/
│       ├── windows/
│       ├── powershell/
│       └── process/
│
├── tests/
│   ├── test_cases/
│   └── expected_results/
│
├── docs/
│   ├── architecture.md
│   ├── detection-development.md
│   ├── testing.md
│   └── mitre-coverage.md
│
├── scripts/
│   └── validate_detections.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

# Detection Workflow

Each detection follows a controlled development lifecycle.

```text
Telemetry
    │
    ▼
Detection Idea
    │
    ▼
Sigma Rule
    │
    ▼
Rule Validation
    │
    ▼
MITRE ATT&CK Mapping
    │
    ▼
KQL Translation
    │
    ▼
Detection Testing
    │
    ▼
Git Commit / Pull Request
    │
    ▼
GitHub Actions
    │
    ▼
Validated Detection
```

---

# Detection Content

## Sigma

Sigma is used as the primary vendor-neutral detection format.

Example categories include:

* Suspicious PowerShell execution
* Process creation anomalies
* File creation activity
* Registry modifications
* DNS activity
* LOLBin execution
* Persistence mechanisms

Sigma rules allow detection logic to remain portable before being converted into platform-specific query languages.

---

## KQL

Kusto Query Language (KQL) is used for Microsoft security telemetry and threat hunting scenarios.

Example data sources may include:

* Windows process telemetry
* Security events
* Sysmon events
* PowerShell telemetry
* DNS activity
* File activity

The KQL detections in this repository are intended to demonstrate how vendor-neutral detection logic can be adapted to Microsoft security telemetry.

---

# MITRE ATT&CK

Detections are mapped to relevant **MITRE ATT&CK techniques and sub-techniques**.

Example mapping:

| Detection             | ATT&CK Technique | Purpose                         |
| --------------------- | ---------------- | ------------------------------- |
| Suspicious PowerShell | T1059.001        | PowerShell execution            |
| Process Discovery     | T1057            | Process enumeration             |
| Registry Run Keys     | T1547.001        | Persistence                     |
| DNS Discovery         | T1016.001        | Network configuration discovery |

MITRE mappings are used to provide detection context and identify areas of coverage.

---

# CI/CD Pipeline

GitHub Actions is used to automate detection validation.

The pipeline is intended to perform checks such as:

```text
Pull Request
     │
     ▼
YAML Validation
     │
     ▼
Sigma Validation
     │
     ▼
Detection Quality Checks
     │
     ▼
Test Execution
     │
     ▼
PASS / FAIL
```

A detection change should not be considered complete until it passes the automated validation process.

---

# Detection Testing

Detection testing is performed using controlled lab activity and security simulation techniques.

Testing may include:

* Atomic Red Team tests
* Controlled PowerShell activity
* Process execution
* File creation
* Registry modification
* DNS activity

Each test documents:

1. Test objective
2. Simulated behavior
3. Expected telemetry
4. Detection logic
5. Expected result
6. Actual result
7. False-positive considerations
8. Limitations

---

# Example Detection Lifecycle

A detection may follow this workflow:

```text
1. Identify suspicious behavior
          ↓
2. Observe endpoint telemetry
          ↓
3. Develop Sigma detection
          ↓
4. Map to MITRE ATT&CK
          ↓
5. Validate Sigma syntax
          ↓
6. Convert/adapt to KQL
          ↓
7. Execute controlled test
          ↓
8. Confirm expected telemetry
          ↓
9. Validate detection
          ↓
10. Commit to Git
          ↓
11. GitHub Actions validation
```

---

# Quality Principles

The project follows several detection engineering principles.

### 1. Version Control

All detection content is stored in Git.

Changes can therefore be:

* Reviewed
* Compared
* Reverted
* Audited
* Tested

### 2. Detection-as-Code

Detection logic is treated as code rather than manually maintained configuration.

### 3. Automated Validation

Detection rules should be automatically checked before being merged.

### 4. Testability

Detections should have a documented method for validating their behavior.

### 5. Documentation

Each detection should explain:

* What it detects
* Why it matters
* Required telemetry
* ATT&CK mapping
* Expected false positives
* Testing methodology
* Limitations

### 6. Maintainability

Rules should be structured consistently so that additional detections can be added without redesigning the repository.

---

# Current Status

| Component               | Status         |
| ----------------------- | -------------- |
| Repository foundation   | 🟡 In Progress |
| Sigma detections        | 🟡 In Progress |
| KQL detections          | 🟡 In Progress |
| MITRE ATT&CK mapping    | 🟡 In Progress |
| Detection tests         | 🟡 In Progress |
| GitHub Actions          | 🟡 In Progress |
| Automated validation    | 🟡 In Progress |
| Portfolio documentation | 🟡 In Progress |

---

# Environment

The project is designed to operate without requiring an active Azure subscription.

### Development Environment

```text
Host OS: Ubuntu Linux
RAM: 32 GB
Storage: 512 GB SSD
Virtualization: VirtualBox
Windows VM: Windows 11 Enterprise
VM RAM: 12 GB
```

Azure and Microsoft Sentinel are **not required for the core pipeline**.

Where applicable, KQL content can be developed and documented independently and later validated against Azure/Microsoft security telemetry when cloud resources become available.

---

# Relationship to Previous Project

This project builds on telemetry and detection engineering work from the Windows Attack Telemetry Research Lab.

Previously developed capabilities include:

* Sysmon telemetry
* Windows Event Viewer
* PowerShell telemetry
* Event ID analysis
* KQL threat hunting
* Sigma rules
* MITRE ATT&CK
* Atomic Red Team
* GitHub documentation

The Detection-as-Code pipeline extends that work by introducing **automation, version control, validation, testing, and CI/CD**.

---

# Future Enhancements

Potential future improvements include:

* Automated Sigma-to-KQL conversion
* Detection unit testing
* Detection coverage dashboards
* MITRE ATT&CK coverage visualization
* Automated rule linting
* Pull-request detection reviews
* False-positive tracking
* Detection performance testing
* Integration with Microsoft Sentinel
* Azure DevOps/GitHub deployment workflows
* Additional telemetry sources

---

# Learning Outcomes

By completing this project, the portfolio demonstrates practical experience with:

* Detection engineering
* Security telemetry analysis
* Sigma
* KQL
* MITRE ATT&CK
* Threat hunting
* Git
* GitHub
* GitHub Actions
* CI/CD
* Automated security validation
* Detection testing
* Blue-team engineering practices

---

# Disclaimer

This project is intended for **authorized security research, defensive security engineering, and educational purposes**.

All testing should be performed against systems and environments that you own or have explicit permission to test.

---

## Project Status

**Project 3 — Detection-as-Code Pipeline**

**Status: 🚧 In Development**

The objective is to create a reproducible, automated, and portfolio-ready detection engineering workflow using open detection standards and Git-based CI/CD.
