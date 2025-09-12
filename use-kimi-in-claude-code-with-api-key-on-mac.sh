#!/bin/bash

# macOS script to configure Claude Code to use Kimi K2 model
# Usage: ./use-kimi-in-claude-code-with-api-key-on-mac.sh

echo "Setting up environment variables for Kimi-K2-Turbo-Preview model..."

# Prompt for API key with secure input (hidden)
echo "Please enter your Moonshot API key:"
read -s API_KEY
echo "✓ API key entered ($(printf '%*s' ${#API_KEY} | tr ' ' '*'))"

echo "Configuring Claude Code to use Kimi K2 model..."

# Set environment variables for Kimi K2
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
export ANTHROPIC_AUTH_TOKEN=$API_KEY
export ANTHROPIC_MODEL=kimi-k2-turbo-preview
export ANTHROPIC_SMALL_FAST_MODEL=kimi-k2-turbo-preview

echo "✓ Set ANTHROPIC_BASE_URL"
echo "✓ Set ANTHROPIC_AUTH_TOKEN (secured)"
echo "✓ Set ANTHROPIC_MODEL to kimi-k2-turbo-preview"
echo "✓ Set ANTHROPIC_SMALL_FAST_MODEL to kimi-k2-turbo-preview"

echo ""
echo "Environment setup complete! You can now use Kimi-K2-Turbo-Preview model with Claude."
echo "Current environment variables:"
echo "ANTHROPIC_BASE_URL: $ANTHROPIC_BASE_URL"
echo "ANTHROPIC_MODEL: $ANTHROPIC_MODEL"
echo "ANTHROPIC_SMALL_FAST_MODEL: $ANTHROPIC_SMALL_FAST_MODEL"

# Launch Claude Code with the configured environment
echo "Launching Claude Code with Kimi K2 configuration..."
claude