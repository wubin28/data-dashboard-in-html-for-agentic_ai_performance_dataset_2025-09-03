# Set environment variables for DeepSeek integration with Claude
Write-Host "Setting up environment variables for DeepSeek Chat model..." -ForegroundColor Green

# Set the base URL for DeepSeek API
$env:ANTHROPIC_BASE_URL = "https://api.deepseek.com/anthropic"
Write-Host "✓ Set ANTHROPIC_BASE_URL" -ForegroundColor Cyan

# Always prompt for API key with secure input
$secureKey = Read-Host "Please enter your DeepSeek API key" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
$apiKey = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
$env:ANTHROPIC_AUTH_TOKEN = $apiKey
Write-Host "✓ Set ANTHROPIC_AUTH_TOKEN (secured)" -ForegroundColor Cyan

# Set API timeout
$env:API_TIMEOUT_MS = "600000"
Write-Host "✓ Set API_TIMEOUT_MS to 600000" -ForegroundColor Cyan

# Set the model names
$env:ANTHROPIC_MODEL = "deepseek-chat"
$env:ANTHROPIC_SMALL_FAST_MODEL = "deepseek-chat"
Write-Host "✓ Set ANTHROPIC_MODEL to deepseek-chat" -ForegroundColor Cyan
Write-Host "✓ Set ANTHROPIC_SMALL_FAST_MODEL to deepseek-chat" -ForegroundColor Cyan

# Disable nonessential traffic
$env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = "1"
Write-Host "✓ Set CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC to 1" -ForegroundColor Cyan

Write-Host "`nEnvironment setup complete! You can now use DeepSeek Chat model with Claude." -ForegroundColor Green
Write-Host "Current environment variables:" -ForegroundColor Yellow
Write-Host "ANTHROPIC_BASE_URL: $env:ANTHROPIC_BASE_URL"
Write-Host "API_TIMEOUT_MS: $env:API_TIMEOUT_MS"
Write-Host "ANTHROPIC_MODEL: $env:ANTHROPIC_MODEL"
Write-Host "ANTHROPIC_SMALL_FAST_MODEL: $env:ANTHROPIC_SMALL_FAST_MODEL"
Write-Host "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: $env:CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"

