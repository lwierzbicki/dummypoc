fetch('http://URL/action',{
    method: 'POST',
    mode: 'same-origin',
    credentials: 'same-origin',
    headers: {
        'Content-Type':'application/x-www-form-urlencoded'
    }, 
    body:'parameter=1&parameter2=&parameter3=aaa'
})
