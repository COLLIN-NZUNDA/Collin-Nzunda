#!/usr/bin/env python3
"""
QR Code Generator for GitHub Repositories
==========================================

This script generates QR codes for GitHub repositories that can be easily
embedded into PowerPoint presentations, posters, or other documents.

Usage:
    python qr_generator.py <repository_url> [output_filename]

Example:
    python qr_generator.py https://github.com/COLLIN-NZUNDA/Collin-Nzunda
    python qr_generator.py https://github.com/username/repo-name custom_qr.png

Author: Collin Nzunda
Project: TP53 and IGHV CLL in Tanzania
"""

import qrcode
import sys
import os
from PIL import Image, ImageDraw, ImageFont
from urllib.parse import urlparse
import argparse


def validate_github_url(url):
    """Validate if the URL is a valid GitHub repository URL."""
    parsed = urlparse(url)
    if parsed.netloc != 'github.com':
        raise ValueError("URL must be a GitHub repository URL")
    
    path_parts = parsed.path.strip('/').split('/')
    if len(path_parts) < 2:
        raise ValueError("Invalid GitHub repository URL format")
    
    return True


def extract_repo_info(url):
    """Extract username and repository name from GitHub URL."""
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    username = path_parts[0]
    repo_name = path_parts[1]
    return username, repo_name


def generate_qr_code(url, output_path=None, add_label=True, size_factor=10):
    """
    Generate a QR code for the given GitHub repository URL.
    
    Args:
        url (str): GitHub repository URL
        output_path (str): Output file path (optional)
        add_label (bool): Whether to add repository label below QR code
        size_factor (int): Size factor for QR code (higher = larger)
    
    Returns:
        str: Path to the generated QR code image
    """
    # Validate URL
    validate_github_url(url)
    
    # Extract repository information
    username, repo_name = extract_repo_info(url)
    
    # Generate default filename if not provided
    if not output_path:
        output_path = f"qr_code_{username}_{repo_name}.png"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size_factor,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    if add_label:
        # Convert QR image to RGB mode first
        if qr_img.mode != 'RGB':
            qr_img = qr_img.convert('RGB')
            
        # Create a new image with space for label
        img_width, img_height = qr_img.size
        label_height = 50
        total_height = img_height + label_height
        
        # Create new image with white background
        final_img = Image.new('RGB', (img_width, total_height), (255, 255, 255))
        
        # Paste QR code at top
        final_img.paste(qr_img, (0, 0))
        
        # Add label
        draw = ImageDraw.Draw(final_img)
        
        # Use default font to avoid complications
        font = ImageFont.load_default()
        
        # Create label text
        label_text = f"{username}/{repo_name}"
        
        # Simple center positioning (approximate)
        text_x = max(10, (img_width - len(label_text) * 6) // 2)  # Approximate character width
        text_y = img_height + 15
        
        # Draw text in black
        draw.text((text_x, text_y), label_text, fill=(0, 0, 0), font=font)
        
        # Save final image
        final_img.save(output_path)
    else:
        # Save QR code without label
        qr_img.save(output_path)
    
    return output_path


def main():
    """Main function to handle command line arguments and generate QR code."""
    parser = argparse.ArgumentParser(
        description="Generate QR codes for GitHub repositories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python qr_generator.py https://github.com/COLLIN-NZUNDA/Collin-Nzunda
  python qr_generator.py https://github.com/username/repo --output custom_qr.png
  python qr_generator.py https://github.com/username/repo --no-label --size 8
        """
    )
    
    parser.add_argument('url', help='GitHub repository URL')
    parser.add_argument('--output', '-o', help='Output filename (optional)')
    parser.add_argument('--no-label', action='store_true', help='Do not add repository label')
    parser.add_argument('--size', type=int, default=10, help='Size factor for QR code (default: 10)')
    
    args = parser.parse_args()
    
    try:
        output_file = generate_qr_code(
            args.url, 
            args.output, 
            add_label=not args.no_label,
            size_factor=args.size
        )
        
        print(f"✅ QR code generated successfully!")
        print(f"📁 File saved as: {output_file}")
        print(f"🔗 Repository: {args.url}")
        
        # Extract repository info for display
        username, repo_name = extract_repo_info(args.url)
        print(f"📊 Repository: {username}/{repo_name}")
        
    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()