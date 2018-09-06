﻿Clear-Variable string2, char, string, integer, decryptedString

# $string = "Lfzcpbse!opu!gpvoe/!Qsftt!G2!up!dpoujovf"
$choose = Read-Host 'decrypt(0) or encrypt(1)?'

if ($choose -eq 0) {
    echo "#Decrypting#"

    $number = Read-Host 'Enter key'

    $encrypting = [boolean]0
} elseif ($choose -eq 1) {
    echo "#Encrypting#"

    $random = Get-Random -Minimum 1 -Maximum 19
    echo "Your key:" $random

    $encrypting = [boolean]1
} else {
    echo "invalid input"
    exit
}

$string = Read-Host 'Write something to encrypt/decrypt'

function decrypt($value) {
    $integer = [int]$value - $number

    $char = [char]$integer

    return $char 
}

function encrypt($value) {
    $integer = [int]$value + $random

    $char = [char]$integer

    return $char
}

for ($i=0; $i -lt $string.Length; $i++) {
    if ($encrypting -eq 0) {
        $string2 = decrypt($string.Chars($i))
    } else {
        $string2 = encrypt($string.Chars($i))
    }

    $decryptedString = $decryptedString + $string2
}

echo $decryptedString