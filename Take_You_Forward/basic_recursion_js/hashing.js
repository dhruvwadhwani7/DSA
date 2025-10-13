arrayOne = [1,2,3,2,1]

function findNuminArray(arr,N){
    let counter = 0
    for (let i=0;i<arr.length;i++){
        if (arr[i] === N){
            counter++
        }
    }
    return counter
}

// console.log(findNuminArray(arrayOne,1))
//___hashing purpose 

function hashingArray(arr,n){
    let hashArray = new Array(13).fill(0);
    for(let i =0 ;i<arr.length;i++){
        let num = arr[i]
        hashArray[num]++
    }
    if (n < hashArray.length){
        return hashArray[n]
    }
    return 0
}

console.log(hashingArray(arrayOne,2)) //2
console.log(hashingArray(arrayOne,1)) //2
console.log(hashingArray(arrayOne,12)) //0
console.log(hashingArray(arrayOne,10)) //0
console.log(hashingArray(arrayOne,4)) //0
console.log(hashingArray(arrayOne,3)) //1