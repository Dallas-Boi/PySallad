// Made 3-9-23 Thursday
// NOTE: This makes the main functions like encryption and ID generation

// Main Const (Non Changeables)
const valid_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(){}:\"<>?,./;'[]+_=-\|`~"

// This Encrypts the given String
function encrypt(string = "") {
    // If the user does not give a String it will throw an error
    if (string == "") {console.error("You must specify a String as \" \" is not valid"); return}

    var new_data = ""
    for (var letter = 0; letter < string.length; letter++) {
        for (var num = 0; num < valid_letters.length; num++) { // Loop for the "valid_letters"
            if (String(string).slice(letter, letter+1) == valid_letters.slice(num, num+1)) {
                if (letter+5 < valid_letters.length) {
                    // If the list does not have to start at the beginning of "valid_letters"
                    new_data += valid_letters.slice(num+5, num+6)
                } else {
                    // If the given letter does have to start at the beginning of "valid_letters"
                    index = letter - len(valid_letters)
                    new_data += valid_letters.slice(index+5, index+6) 
                }
            } 
        }
    }

    return new_data
}

// This Decrypts the given String
function decrypt(string = "") {
    // If the user does not give a String it will throw an error
    if (string == "") {console.error("You must specify a String as \" \" is not valid"); return}

    var new_data = ""
    for (var letter = 0; letter < string.length; letter++) {
        for (var num = 0; num < valid_letters.length; num++) { // Loop for the "valid_letters"
            if (String(string).slice(letter, letter+1) == valid_letters.slice(num, num+1)) {
                if (letter+5 < valid_letters.length) {
                    // If the list does not have to start at the beginning of "valid_letters"
                    new_data += valid_letters.slice(num-5, num-4)
                } else {
                    // If the given letter does have to start at the beginning of "valid_letters"
                    index = len(valid_letters) - letter
                    new_data += valid_letters.slice(index-5, index-4) 
                }
            } 
        }
    }

    return new_data
}

var en = encrypt("aaa")
var de = decrypt(en)

console.log(en)
console.log(de)