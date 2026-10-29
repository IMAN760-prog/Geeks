const promise = new Promise((resolve)=>{
    setTimeout(() => {
        resolve("success");
    },4000);
    
})
promise.then(resolte => console.log(resolte));