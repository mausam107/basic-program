let arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8, 9, [12, 23, 21], [11, 33, 44, 55], [100]],
    [99]
  ];
let arr2=[]
for(let i=0;i<arr.length;i++){
    for(let j=0;j<arr[i].length;j++){
        // arr2.push(arr[i][j]);
        if(!Array.isArray(arr[i][j])){
            arr2.push(arr[i][j]);

            }
        if(Array.isArray(arr[i][j])){
            for(let k=0;k<arr[i][j].length;k++){
                arr2.push(arr[i][j][k])
            }

        }
        
        
    }
    
}
console.log(arr2);