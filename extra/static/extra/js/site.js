function fetch(filter, callback) {
  $.ajax({
    url: '/stream/',
    data: filter,
    success: function(data) {
      if (typeof callback === 'function') {
        callback(data);
      }
    }
  });
}

// Polling
let filter = {'pk__gt': 0, 'pk__lt': 100};
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
