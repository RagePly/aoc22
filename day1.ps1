$content = Get-Content -Raw .\day1.txt
$calories = New-Object System.Collections.Generic.List[Int32]

foreach ($line in $content.Split("`r`n`r`n")) {
    $s = 0
    foreach($c in $line.Split("`r`n", [System.StringSplitOptions]::RemoveEmptyEntries)) {
        $s += [System.Convert]::ToInt32($c)
    }
    $calories.Add($s)
}

$calories.Sort()
$l = $calories.Count

Write-Output $calories[$l - 1]
Write-Output ($calories[$l - 1] + $calories[$l - 2] + $calories[$l - 3])