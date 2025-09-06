# Set environment variables for Kimi integration with Claude
Write-Host "Setting up environment variables for Kimi-K2-Turbo-Preview model..." -ForegroundColor Green

# Set the base URL for Moonshot API
$env:ANTHROPIC_BASE_URL = "https://api.moonshot.cn/anthropic"
Write-Host "✓ Set ANTHROPIC_BASE_URL" -ForegroundColor Cyan

# Always prompt for API key with secure input
$secureKey = Read-Host "Please enter your Moonshot API key" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
$apiKey = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
$env:ANTHROPIC_AUTH_TOKEN = $apiKey
Write-Host "✓ Set ANTHROPIC_AUTH_TOKEN (secured)" -ForegroundColor Cyan

# Set the model names
$env:ANTHROPIC_MODEL = "kimi-k2-turbo-preview"
$env:ANTHROPIC_SMALL_FAST_MODEL = "kimi-k2-turbo-preview"

Write-Host "✓ Set ANTHROPIC_MODEL to kimi-k2-turbo-preview" -ForegroundColor Cyan
Write-Host "✓ Set ANTHROPIC_SMALL_FAST_MODEL to kimi-k2-turbo-preview" -ForegroundColor Cyan

Write-Host "`nEnvironment setup complete! You can now use Kimi-K2-Turbo-Preview model with Claude." -ForegroundColor Green
Write-Host "Current environment variables:" -ForegroundColor Yellow
Write-Host "ANTHROPIC_BASE_URL: $env:ANTHROPIC_BASE_URL"
Write-Host "ANTHROPIC_MODEL: $env:ANTHROPIC_MODEL"
Write-Host "ANTHROPIC_SMALL_FAST_MODEL: $env:ANTHROPIC_SMALL_FAST_MODEL"
