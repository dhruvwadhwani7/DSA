function factorial(N){
    let fact = 1 
    for (let i = 1;i<=N;i++){
        fact = (fact * i)
    }
    console.log(fact)
}
// factorial(2)
// factorial(5)

function recursiveFactorial(N){
    if(N === 0){
        return 1
    }
    return N * recursiveFactorial(N-1)
}
console.log(recursiveFactorial(5))
console.log(recursiveFactorial(0))
console.log(recursiveFactorial(1))