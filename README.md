### GT Assigment

# 📌 Frappe HRMS Customization – Developer Assignment

## 🎯 Objective
This repository contains the implementation of the Frappe Developer Assignment.  
The project extends **Frappe Framework** and **ERPNext HRMS module** to cover **Recruitment, Employee Lifecycle, Payroll, Taxation, and Customizations**.  
It also demonstrates **Git best practices** with feature branching, pull requests, and structured commits.

---

## 🏗️ Features Implemented

### 1. HRMS & Recruitment
- ✅ Custom **Recruitment Workflow**:  
  `Job Opening → Application → Screening → Interview → Offer → Hired`
- ✅ Configured **role-based permissions** for:  
  HR Manager, Interviewer, Hiring Manager
- ✅ Added custom field in **Job Applicant**: *Source of Application* (LinkedIn, Referral, Job Portal, etc.)
- ✅ Built **report/dashboard** showing applicants per source

---

### 2. Employee Lifecycle
- ✅ Configured **Employee Doctype lifecycle**: `Joining → Probation → Confirmation → Exit`
- ✅ Automation:  
  - On **Confirmation** → Auto-update employee status  
  - On **Exit** → Generate **Experience Letter** (PDF)

---

### 3. Salary Structure & Payroll
- ✅ Created **Salary Structure** with:  
  *Basic, HRA, Special Allowance, PF, Professional Tax*
- ✅ Configured **Earnings & Deductions**
- ✅ Implemented **Payroll Entry** for multiple employees
- ✅ Designed **custom Payroll Slip print format** with branding

---

### 4. Tax Regime Implementation
- ✅ Support for **Old & New Tax Regimes**  
- ✅ Two separate Salary Structures (Old Regime, New Regime)  
- ✅ Added custom field in **Employee Doctype**: *Tax Regime Preference*  
- ✅ On Payroll Run → System picks correct salary structure based on preference  
- ✅ **Comparison Report**: Old vs New Tax Deduction

---

### 5. Customization
- ✅ Created **Custom Doctype**: *Employee Investment Declaration* with fields:  
  - Section 80C (LIC, PPF, ELSS, etc.)  
  - Section 80D (Medical Insurance)  
  - Other Exemptions  
- ✅ Integrated with Payroll for **tax calculation adjustments**

---

### 6. GitHub & Version Control
- ✅ Used **feature branches** (e.g., `feature/tax-regime`, `feature/recruitment-workflow`)  
- ✅ Created **Pull Requests** for merging into `main` (no direct merges)  
- ✅ Followed **commit best practices** with meaningful messages  



### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app gt_assigment
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/gt_assigment
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
