let count = 0 

function nTimes(){
    if(count == 3){
        return
    }
    console.log(count)
    count ++
    nTimes()
}
// nTimes()

function myNameNTimes(str,n){
    if(n === 0 ) return;
    console.log(str)
    myNameNTimes(str,n-1)
}
// myNameNTimes('Dhruv',3)
// myNameNTimes('Dhruv',0)

function NTimes(num){
    if(num === 0 ) return;
    NTimes(num-1)
    console.log(num)
}
// NTimes(4)

function TimesN(num){
    if(num==0){
        return
    }
    console.log(num)
    TimesN(num-1)
}
TimesN(4)