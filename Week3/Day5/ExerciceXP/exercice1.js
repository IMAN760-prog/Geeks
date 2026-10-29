function compareToTen(num){
  const promise = new Promise((resolve, reject) => {
   if (num<=10){
    resolve("It's great");
  }else {
    reject(new Error("Loading failed"));
  }

  });
   return promise;
  }
compareToTen(8)
.then(resolt => console.log(resolt))
.catch(error => console.log(error.message));
 