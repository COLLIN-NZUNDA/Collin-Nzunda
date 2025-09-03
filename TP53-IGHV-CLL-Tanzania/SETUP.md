# Quick Setup Guide

## Getting Started with TP53-IGHV-CLL-Tanzania Project

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or navigate to the repository:**
   ```bash
   cd TP53-IGHV-CLL-Tanzania
   ```

2. **Install required packages:**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.py
   ```

### Quick Start

#### Generate QR Code for Your Repository
```bash
cd scripts
python3 qr_generator.py https://github.com/YOUR-USERNAME/YOUR-REPO --output ../images/my_qr.png
```

#### Generate Example QR Codes
```bash
cd scripts
python3 generate_examples.py
```

#### View Generated QR Codes
```bash
ls -la images/
```

### Usage Examples

1. **Basic QR code:**
   ```bash
   python3 scripts/qr_generator.py https://github.com/COLLIN-NZUNDA/Collin-Nzunda
   ```

2. **QR code for presentations:**
   ```bash
   python3 scripts/qr_generator.py https://github.com/COLLIN-NZUNDA/TP53-IGHV-CLL-Tanzania --output images/presentation.png
   ```

3. **Large QR code for posters:**
   ```bash
   python3 scripts/qr_generator.py https://github.com/COLLIN-NZUNDA/TP53-IGHV-CLL-Tanzania --size 15 --output images/poster.png
   ```

### Next Steps

1. Read the full [PowerPoint Integration Guide](docs/powerpoint_integration.md)
2. Explore the [main project README](README.md)
3. Generate QR codes for your specific repositories
4. Add QR codes to your presentations and posters

### Support

For questions or issues:
- Email: collin.nzunda@muhas.ac.tz
- GitHub: [COLLIN-NZUNDA](https://github.com/COLLIN-NZUNDA)