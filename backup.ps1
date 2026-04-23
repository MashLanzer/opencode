# backup.ps1
# Respaldo automático del proyecto a GitHub
# Ejecutar al final de cada sesión o manualmente

param(
    [string]$GitHubOrg = "MashLanzer",
    [string]$GitHubRepo = "opencode",
    [string]$Branch = "master",
    [switch]$Auto = $false
)

$ErrorActionPreference = "Stop"
$date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$shortDate = Get-Date -Format "yyyy-MM-dd"

Write-Host "=== Respaldo OpenCode ===" -ForegroundColor Cyan
Write-Host "Fecha: $date" -ForegroundColor Gray

# Cambiar al directorio del proyecto
Set-Location "C:\Users\braya\opencode"

# Verificar si hay cambios
$status = git status --porcelain
if ($status) {
    Write-Host "Cambios detectados: $(($status | Measure-Object).Count) archivos" -ForegroundColor Yellow
    
    # Stage all files
    git add -A
    
    # Commit con fecha
    $commitMsg = "Backup: $shortDate"
    git commit -m $commitMsg
    
    # Push to GitHub
    Write-Host "Subiendo a GitHub..." -ForegroundColor Cyan
    git push origin $Branch
    
    Write-Host "Backup completado: $date" -ForegroundColor Green
    
    # Registrar en OMI
    try {
        $omiHeaders = @{
            "Authorization" = "Bearer omi_dev_f109295456f5a35b2226ddadc206b4dc"
            "Content-Type" = "application/json"
        }
        
        $memory = @{
            content = "Backup automatico a GitHub completado: $date"
            category = "system"
            tags = @("opencode", "backup")
        } | ConvertTo-Json
        
        Invoke-WebRequest -Uri "https://api.omi.me/v1/dev/user/memories" -Method POST -Headers $omiHeaders -Body $memory -UseBasicParsing -TimeoutSec 15 | Out-Null
        Write-Host "Sincronizado con OMI" -ForegroundColor Green
    } catch {
        Write-Host "OMI sync fallido (no critico)" -ForegroundColor Yellow
    }
    
    # Actualizar nota de backup
    try {
        $backupNote = @"
---
tags: [backup, historial]
creado: $shortDate
actualizado: $shortDate
---

# Historial de Backups

## Registro

### $shortDate
- Estado: Exitoso
- Archivos: $(($status | Measure-Object).Count)
- Commit: $commitMsg

---
*Actualizado automaticamente*
"@
        
        $null = Invoke-WebRequest -Uri "http://127.0.0.1:27123/vault/Notas/backup/historial.md" -Method PUT -Headers @{"Authorization"="Bearer dadde3d8184f6aae78239eb4570ac4430b55532fcf5afb77fd081f70c7e0c459"; "Content-Type"="text/markdown"} -Body $backupNote -UseBasicParsing -TimeoutSec 10
    } catch {
        Write-Host "Nota backup no actualizada" -ForegroundColor Yellow
    }
    
    Write-Host ""
    Write-Host "=== RESPALDO COMPLETADO ===" -ForegroundColor Green
    exit 0
    
} else {
    Write-Host "No hay cambios para respaldar" -ForegroundColor Gray
    Write-Host ""
    Write-Host "=== RESPALDO COMPLETADO (sin cambios) ===" -ForegroundColor Green
    exit 0
}