var fibRecurcive = function(n) {
    if (n<2) return n;
    return fib(n-1) + fib(n-2)
};
console.log(fibRecurcive(2))

var fib = function(n) {
    if (n<2) return n;
    let a=0, b=1;
    for (let i = 2;i<=n;i++){
        let temp = a + b
        a = b
        b = temp 
    }
    return b
};
console.log(fib(2))

