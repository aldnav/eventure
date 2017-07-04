function fetch(filter, callback) {
  var filters = getFilter(filter);
  var request = new XMLHttpRequest();
  request.open('GET', `/stream/?${filters}`, true);

  request.onload = () => {
    if (request.status >= 200 && request.status < 400) {
      if (typeof callback === 'function') {
        callback(request.responseText);
      }
    }
  }
  request.send();
}

function serialize(obj) {
  var str = [];
  for(var p in obj)
     str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
  return str.join("&");
}

function getFilter(filters) {
  return serialize({filters: JSON.stringify(filters)});
}

// Polling
let filter = {'pk__gt':0, 'pk__lt': 100};
// 1. Single Fetch
fetch(filter, (response) => {
  console.log(response);
});

// 2. Update filter accordingly
// fetch(filter, (response) => {
//   console.log(response);
// });

// Long polling
// 3. Set timeout
