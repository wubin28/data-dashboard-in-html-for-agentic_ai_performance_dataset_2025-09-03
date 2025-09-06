# Set environment variables for GLM integration with Claude
Write-Host "Setting up environment variables for GLM model..." -ForegroundColor Green

# Set the base URL for GLM API
$env:ANTHROPIC_BASE_URL = "https://open.bigmodel.cn/api/anthropic"
Write-Host "✓ Set ANTHROPIC_BASE_URL" -ForegroundColor Cyan

# Always prompt for API key with secure input
$secureKey = Read-Host "Please enter your GLM API key" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureKey)
$apiKey = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
$env:ANTHROPIC_AUTH_TOKEN = $apiKey
Write-Host "✓ Set ANTHROPIC_AUTH_TOKEN (secured)" -ForegroundColor Cyan

# Set the model names
$env:ANTHROPIC_MODEL = "glm-4"
$env:ANTHROPIC_SMALL_FAST_MODEL = "glm-3-turbo"

Write-Host "✓ Set ANTHROPIC_MODEL to glm-4" -ForegroundColor Cyan
Write-Host "✓ Set ANTHROPIC_SMALL_FAST_MODEL to glm-3-turbo" -ForegroundColor Cyan

Write-Host "`nEnvironment setup complete! You can now use GLM models with Claude." -ForegroundColor Green
Write-Host "Current environment variables:" -ForegroundColor Yellow
Write-Host "ANTHROPIC_BASE_URL: $env:ANTHROPIC_BASE_URL"
Write-Host "ANTHROPIC_MODEL: $env:ANTHROPIC_MODEL"
Write-Host "ANTHROPIC_SMALL_FAST_MODEL: $env:ANTHROPIC_SMALL_FAST_MODEL"
