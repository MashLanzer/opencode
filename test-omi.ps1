$headers = @{
    "Authorization" = "Bearer omi_dev_f109295456f5a35b2226ddadc206b4dc"
    "Content-Type" = "application/json"
}
$body = @{
    content = "OpenCode connected to Obsidian via Local REST API. Memory system active."
    category = "system"
    tags = @("opencode", "obsidian")
} | ConvertTo-Json

Invoke-WebRequest -Uri "https://api.omi.me/v1/dev/user/memories" -Method POST -Headers $headers -Body $body -UseBasicParsing -TimeoutSec 15