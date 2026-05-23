param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$RemainingArgs
)

$repoRoot = Split-Path -LiteralPath $PSCommandPath -Parent
$noClobber = $false
$urls = @()

foreach ($arg in $RemainingArgs) {
    switch ($arg) {
        '-q' { continue }
        '-nc' {
            $noClobber = $true
            continue
        }
        '-N' {
            $noClobber = $true
            continue
        }
        default {
            if ($arg.StartsWith('-')) {
                continue
            }

            $urls += $arg.Trim([char]34, [char]39)
        }
    }
}

if (-not $urls) {
    Write-Error 'wget shim requires a URL argument.'
    exit 2
}

$url = $urls[-1]
$uri = [Uri]$url
$targetName = [System.IO.Path]::GetFileName($uri.AbsolutePath)

if (-not $targetName) {
    Write-Error "Unable to determine a target filename from URL: $url"
    exit 2
}

$destination = Join-Path -Path (Get-Location) -ChildPath $targetName

if ($noClobber -and (Test-Path -LiteralPath $destination)) {
    exit 0
}

$knownRepoPrefixes = @(
    'https://github.com/brendanpshea/database_sql/raw/main/',
    'https://raw.githubusercontent.com/brendanpshea/database_sql/main/'
)

$localSource = $null

foreach ($prefix in $knownRepoPrefixes) {
    if ($url.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        $relativePath = $url.Substring($prefix.Length).Replace('/', [System.IO.Path]::DirectorySeparatorChar)
        $candidate = Join-Path -Path $repoRoot -ChildPath $relativePath

        if (Test-Path -LiteralPath $candidate) {
            $localSource = $candidate
            break
        }
    }
}

if ($localSource) {
    $resolvedSource = (Resolve-Path -LiteralPath $localSource).Path
    $resolvedDestination = [System.IO.Path]::GetFullPath($destination)

    if ($resolvedSource -ne $resolvedDestination) {
        Copy-Item -LiteralPath $resolvedSource -Destination $resolvedDestination -Force
    }

    exit 0
}

Invoke-WebRequest -Uri $url -OutFile $destination