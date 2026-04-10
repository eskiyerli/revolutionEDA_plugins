#!/usr/bin/env python3
"""
Scan plugin directories and regenerate plugins.json based on discovered artifacts.

Each plugin directory is expected to contain:
- For source plugins: <plugin_name>.zip
- For binary plugins: <platform>.zip files (e.g., linux-x86_64-py3.13.zip)

Plugin metadata is defined in PLUGIN_DEFINITIONS below.
"""

import json
import os
import re
from pathlib import Path

# Base URL for raw GitHub content
RAW_URL = "https://raw.githubusercontent.com/eskiyerli/revolutionEDA_plugins/main"

# Plugin metadata definitions - edit this to add/modify plugins
PLUGIN_DEFINITIONS = {
    "aiTerminal": {
        "license": "Mozilla Public License 2.0",
        "type": "source",
        "description": "AI Terminal plugin for Revolution EDA. Integrates AI agents (Claude, Gemini) for design assistance and automation.",
    },
    "revedasim": {
        "license": "Proprietary",
        "type": "binary",
        "description": "Simulation plugin for Revolution EDA using Xyce simulator. Provides netlisting and simulation capabilities for schematic designs.",
    },
    "revedaPlot": {
        "license": "Proprietary",
        "type": "binary",
        "description": "Plotting plugin for Revolution EDA. Enables visualization of simulation results using PyQtGraph.",
    },
}

# Regex patterns for platform detection
PLATFORM_PATTERNS = {
    r"linux-x86_64-py3\.13\.zip": "linux-x86_64-py3.13",
    r"linux-x86_64-py313\.zip": "linux-x86_64-py313",
    r"windows-amd64-py3\.13\.zip": "windows-amd64-py3.13",
    r"windows-x64-py313\.zip": "windows-x64-py313",
    r"macos-x86_64-py3\.13\.zip": "macos-x86_64-py3.13",
    r"macos-amd64-py3\.13\.zip": "macos-amd64-py3.13",
}

# Version extraction from directory scanning or fallback
VERSION_FALLBACK = {
    "aiTerminal": "0.1.0",
    "revedasim": "0.8.10",
    "revedaPlot": "0.8.10",
}


def extract_version_from_zip_name(filename: str) -> str | None:
    """Try to extract version from zip filename like plugin-v1.2.3.zip"""
    match = re.search(r"[-_](\d+\.\d+(?:\.\d+)?)", filename)
    if match:
        return match.group(1)
    return None


def detect_platform(filename: str) -> str | None:
    """Detect platform from zip filename."""
    for pattern, platform in PLATFORM_PATTERNS.items():
        if re.search(pattern, filename, re.IGNORECASE):
            return platform
    return None


def scan_plugin_directory(plugin_dir: Path) -> dict:
    """Scan a plugin directory and return its metadata."""
    plugin_name = plugin_dir.name

    if plugin_name not in PLUGIN_DEFINITIONS:
        print(f"Warning: No metadata defined for plugin '{plugin_name}', skipping")
        return None

    meta = PLUGIN_DEFINITIONS[plugin_name].copy()
    meta["name"] = plugin_name

    # Determine version
    version = VERSION_FALLBACK.get(plugin_name, "0.0.0")

    # For source plugins, look for <plugin_name>.zip
    if meta["type"] == "source":
        source_zip = plugin_dir / f"{plugin_name}.zip"
        if source_zip.exists():
            extracted_version = extract_version_from_zip_name(source_zip.name)
            if extracted_version:
                version = extracted_version
            meta["url"] = f"{RAW_URL}/{plugin_name}/{source_zip.name}"
        else:
            print(f"Warning: Source zip not found for '{plugin_name}'")
            return None

    # For binary plugins, look for platform-specific zips
    elif meta["type"] == "binary":
        binary_urls = {}
        for zip_file in plugin_dir.glob("*.zip"):
            platform = detect_platform(zip_file.name)
            if platform:
                binary_urls[platform] = f"{RAW_URL}/{plugin_name}/{zip_file.name}"
                # Try to extract version from filename
                extracted_version = extract_version_from_zip_name(zip_file.name)
                if extracted_version:
                    version = extracted_version

        if not binary_urls:
            print(f"Warning: No platform zips found for '{plugin_name}'")
            return None

        meta["binary_urls"] = binary_urls

    meta["version"] = version

    return meta


def generate_plugins_json():
    """Main entry point to scan and generate plugins.json."""
    repo_root = Path(__file__).parent.parent.parent
    plugins_dir = repo_root

    plugins = []

    # Scan for plugin directories
    for item in sorted(plugins_dir.iterdir()):
        if item.is_dir() and not item.name.startswith(".") and item.name != ".github":
            plugin_data = scan_plugin_directory(item)
            if plugin_data:
                plugins.append(plugin_data)
                print(f"Found plugin: {plugin_data['name']} v{plugin_data['version']}")

    # Build final structure
    output = {"plugins": plugins}

    # Write to plugins.json
    output_path = repo_root / "plugins.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    print(f"\nGenerated plugins.json with {len(plugins)} plugin(s)")
    return output


if __name__ == "__main__":
    generate_plugins_json()
