let s =  "A man, a plan, a canal: Panama"

function isPalindromeNew(str){
    let cleanedString = str.toLowerCase().replace(/[^a-z0-9]/g,'')
    console.log(cleanedString,cleanedString.length)
    let leftP = 0
    let rightP  = cleanedString.length - 1

    while (leftP<rightP){
        if(cleanedString[leftP] !== cleanedString[rightP]){
            return false
        }
        leftP++
        rightP--
    }
    return true
}
// console.log(isPalindromeNew(s))


//LEETCODE
var isPalindrome = function(str) {
    let cleanedString = str.toLowerCase().replace(/[^a-z0-9]/g,'')
    console.log(cleanedString,cleanedString.length)
    let leftP = 0
    let rightP  = cleanedString.length - 1

    while (leftP<rightP){
        if(cleanedString[leftP] !== cleanedString[rightP]){
            console.log(false)
        }
        leftP++
        rightP--
    }
    console.log(true)
};
isPalindrome(s)