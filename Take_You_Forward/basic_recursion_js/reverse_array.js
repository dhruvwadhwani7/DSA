let arrayOne = [1,2,3,4,5]

function reverseArray(arr){
    finalArray = []
    for (let i = arr.length-1;i>=0;i--){
        finalArray.push(arr[i])
    }
    console.log(finalArray)
}

// reverseArray(arrayOne)
// reverseArray([10,20,30,40])

// ______2 pointers approach___

// console.log(arrayOne.length)
function twoPointerReverseArray(arr){
    let leftP = 0
    let rightP = arr.length - 1
    while (leftP < rightP){ 
        [arr[leftP],arr[rightP]] = [arr[rightP],arr[leftP]] //destructuring [] = [] comparison
        leftP = leftP +  1 
        rightP = rightP - 1
    }
    console.log(arr)
}
twoPointerReverseArray(arrayOne)