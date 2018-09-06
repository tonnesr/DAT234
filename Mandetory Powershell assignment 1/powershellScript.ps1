Clear-Variable string2, char, string, integer, decryptedString

$string = "Lfzcpbse!opu!gpvoe/!Qsftt!G2!up!dpoujovf"

function decrypt($value) {
    $integer = [int]$value - 1

    $char = [char]$integer

    return $char 
}

for ($i=0; $i -lt $string.Length; $i++) {
    $string2 = decrypt($string.Chars($i))

    $decryptedString = $decryptedString + $string2
}

echo $decryptedString