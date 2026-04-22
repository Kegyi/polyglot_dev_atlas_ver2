# Copy TypeScript example files from polyglot_dev_atlas/code_examples
$src = "c:\\Users\\Kegyi\\C++\\TestProject\\polyglot_dev_atlas\\code_examples"
$dst = "c:\\Users\\Kegyi\\C++\\TestProject\\polyglot_dev_atlas_ver2\\content\\snippets\\typescript"

New-Item -ItemType Directory -Force -Path $dst | Out-Null

# Copy files literally named "typescript.ts" using parent folder name
Get-ChildItem -Path $src -Recurse -Filter "typescript.ts" -File | ForEach-Object {
    $parent = Split-Path $_.DirectoryName -Leaf
    $target = Join-Path $dst ("$parent.ts")
    Copy-Item -Path $_.FullName -Destination $target -Force
    Write-Output $target
}

# Also copy files that include "_typescript" in their filename and remove the suffix
Get-ChildItem -Path $src -Recurse -File | Where-Object { $_.Name -match "_typescript" } | ForEach-Object {
    $name = $_.BaseName -replace "_typescript$", ""
    $ext = $_.Extension
    $target = Join-Path $dst ("$name$ext")
    Copy-Item -Path $_.FullName -Destination $target -Force
    Write-Output $target
}

Write-Output "Done."
