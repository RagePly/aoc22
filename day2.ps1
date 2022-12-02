$content = Get-Content -Raw .\input\day2.txt
$lines = $content.Split("`r`n", [System.StringSplitOptions]::RemoveEmptyEntries)

$points1 = 0
$points2 = 0

foreach($line in $lines) {
    $strategies = $line.Split(" ")
    $op = "ABC".IndexOf($strategies[0])
    $me = "XYZ".IndexOf($strategies[1])

    $points1 += $me + 1
    if ($op -eq $me) {
        $points1 += 3
    } elseif (($op + 1) % 3 -eq $me) {
        $points1 += 6
    }
    
    if ($me -eq 0) {
        $points2 += ($op + 2) % 3 + 1
    } elseif ($me -eq 1) {
        $points2 += 3 + $op + 1
    } else {
        $points2 += 6 + ($op + 1) % 3 + 1
    }
}

Write-Output $points1
Write-Output $points2