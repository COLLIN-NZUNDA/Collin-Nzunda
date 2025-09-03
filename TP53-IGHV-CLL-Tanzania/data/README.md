# Data Directory

This directory is intended to store research data for the TP53 and IGHV CLL study in Tanzania.

## Directory Structure

```
data/
├── clinical/          # Clinical patient data
├── molecular/         # Molecular analysis results
├── raw/              # Raw sequencing data
├── processed/        # Processed and analyzed data
└── metadata/         # Sample metadata and annotations
```

## Data Privacy and Ethics

⚠️ **Important:** This directory should contain **NO patient-identifiable information**.

- All data files are excluded from version control via `.gitignore`
- Follow institutional guidelines for data handling
- Ensure proper anonymization of patient data
- Obtain appropriate ethical approvals before data collection

## Data Format Guidelines

### Clinical Data
- Use standardized formats (CSV, Excel)
- Include data dictionaries
- Anonymize patient identifiers

### Molecular Data
- Standard formats: VCF, BED, FASTA
- Include analysis parameters
- Document software versions used

### Metadata
- Link samples to clinical data via anonymous IDs
- Include collection dates and methods
- Document storage conditions

## Access and Sharing

- Follow institutional data sharing policies
- Ensure compliance with ethics committee requirements
- Consider international guidelines for genomic data sharing

---

**Note:** Actual data files are not included in this repository for privacy and ethical reasons.