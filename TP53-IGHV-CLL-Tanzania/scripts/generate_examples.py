#!/usr/bin/env python3
"""
Example Usage of QR Code Generator
=================================

This script demonstrates various ways to use the QR code generator
for different presentation needs.
"""

import subprocess
import os
import sys

def run_qr_generator(url, output_path, extra_args=None):
    """Helper function to run the QR generator with error handling."""
    cmd = ['python3', 'qr_generator.py', url, '--output', output_path]
    if extra_args:
        cmd.extend(extra_args)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Generated: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating {output_path}: {e.stderr}")
        return False

def main():
    """Generate example QR codes for different use cases."""
    
    # Change to scripts directory
    if not os.path.exists('qr_generator.py'):
        print("❌ Please run this script from the scripts/ directory")
        sys.exit(1)
    
    print("🎯 Generating example QR codes...")
    print("="*50)
    
    # Repository URL
    repo_url = "https://github.com/COLLIN-NZUNDA/TP53-IGHV-CLL-Tanzania"
    
    examples = [
        {
            'name': 'Standard QR Code with Label',
            'output': '../images/example_standard.png',
            'args': []
        },
        {
            'name': 'Clean QR Code (No Label)',
            'output': '../images/example_clean.png',
            'args': ['--no-label']
        },
        {
            'name': 'Large QR Code for Posters',
            'output': '../images/example_poster.png',
            'args': ['--size', '15']
        },
        {
            'name': 'Small QR Code for Cards',
            'output': '../images/example_small.png',
            'args': ['--size', '6', '--no-label']
        },
        {
            'name': 'Profile Repository QR',
            'output': '../images/example_profile.png',
            'args': []
        }
    ]
    
    # Generate different examples
    success_count = 0
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['name']}")
        
        # Use profile URL for the last example
        url = "https://github.com/COLLIN-NZUNDA/Collin-Nzunda" if i == len(examples) else repo_url
        
        if run_qr_generator(url, example['output'], example['args']):
            success_count += 1
    
    print("\n" + "="*50)
    print(f"✅ Successfully generated {success_count}/{len(examples)} QR codes")
    
    if success_count == len(examples):
        print("\n📁 Check the ../images/ directory for all generated QR codes")
        print("📖 See ../docs/powerpoint_integration.md for usage instructions")
    else:
        print("\n⚠️  Some QR codes failed to generate. Check error messages above.")

if __name__ == "__main__":
    main()