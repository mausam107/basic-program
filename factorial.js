function fac(n){
    if(n === 1){
        return 1;
    }
    return n*fac(n-1);
}

var factorial= fac(4);
console.log(factorial);