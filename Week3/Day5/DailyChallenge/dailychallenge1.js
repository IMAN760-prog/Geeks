function makeAllCaps(words){
   return new Promise((resolve, reject) => {
        if (words.every(word=>typeof word=== "string")){
            resolve(words.map(word=>word.toUpperCase()))
}       else{
          reject (new Error("All elements must be string "))
         }
   
        });
    }

function sortWords(words){
    return new Promise((resolve,reject)=>{
        if(words.length>4){
            resolve(words.sort())

        }else{
            reject(new Error("The array must contain more than 4 words"));
        }
    });
    
}
     

makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
.then((arr) => sortWords(arr))
.then(resolt => console.log(resolt))
.catch(error => console.log(error.message));