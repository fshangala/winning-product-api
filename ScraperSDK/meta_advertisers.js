var table = document.querySelector("#store-table");
var data=[];
for(var i=1;i<table.rows.length;i++){
  var row={
    "page":{
      "url":table.rows[i].cells[0].querySelector("a").getAttribute("href"),
      "picture_url":table.rows[i].cells[0].querySelector("a img").getAttribute("src"),
      "name":table.rows[i].cells[0].querySelector("a div").innerText
    },
    "countries":Array.from(table.rows[i].cells[1].querySelectorAll("img")).map((value)=>value.getAttribute("src")),
    "website":Array.from(table.rows[i].cells[2].querySelectorAll("img")).map((value)=>value.getAttribute("src")),
    "ads":table.rows[i].cells[3].innerText,
    "adsets":table.rows[i].cells[4].innerText,
    "avgAdsets":table.rows[i].cells[5].innerText,
    "likes":table.rows[i].cells[6].innerText,
    "followers":table.rows[i].cells[7].innerText,
    "created":table.rows[i].cells[8].innerText
  };
  data.push(row);
};
return data;