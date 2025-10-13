// Given a number ‘N’, find out the sum of the first N natural numbers.

function sumOfnNatural(n){
    let sum = 0
    for(let i = 0 ; i<=n ; i++){
        sum = sum + i
    }
    console.log(sum)
}
// sumOfnNatural(5)

function sumOfNaturalNumber(N){
    if(N===0){
        return 0
    }
    return  N  + sumOfNaturalNumber(N-1)
    
}
console.log(sumOfNaturalNumber(5))