let scihubAddr = "https://sci-hub.se/";
let corsProxy = "http://localhost:3000/pipe/";
let logoAddr = chrome.runtime.getURL(`pigeon.png`);
let headerExclusion = ["[B]", "[PDF]"];

function checkUnavailableLink(item, url) {
    header = item.getElementsByClassName("gs_ct2");

    if (header.length == 0) {
        return true;
    } else{
        var length = headerExclusion.length;
        while(length--) {
               if (header[0].innerText.indexOf(headerExclusion[length])!=-1) {
                          // one of the substrings is in yourstring
                    return false;
               }
        }     
    }       

    return true;
}

function getScihubLinkElement(url){
    var result = document.createElement("div");
    result.className = "gs_ggs gs_fl";
    result.innerHTML = `<div class="gs_ggsd"><div class="gs_or_ggsm" ontouchstart="gs_evt_dsp(event)" tabindex="-1">
                         <a href='${scihubAddr + url}'>
                         <span class="gs_ctg2"><img width='16px' src='${logoAddr}'/></span>
                        find @ sci-hub</a></div></div>`;
    return result;
}

function checkResourceLink(item) {
    if (item.getElementsByClassName("gs_ggs gs_fl").length > 0){
        return false;
    }
    return true;
}

function getDOIFromPage(url) {
    // $.get( url, function( data ) {
    //     console.log(data);     
    // });

    console.log(corsProxy+url);

    fetch(corsProxy+url, {mode: 'no-cors'}).then(
        function(response) {            
            if (response.status == 200) {
                console.log(response.text);
            }
        }
    );

    return false;
}


function processGoogleScholarPage (res){
    var i = 0;
    for (; i< res.length; i++){        
        item = res[i].getElementsByClassName("gs_rt")[0];        
        if (checkResourceLink(res[i])) {

            url = item.getElementsByTagName("a")[0].href;
            getDOIFromPage(url);
            res[i].insertBefore(getScihubLinkElement(url), res[i].firstChild);
        }
    }
}

res = document.getElementsByClassName("gs_r gs_or gs_scl");
processGoogleScholarPage(res);