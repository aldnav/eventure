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
let filter = {'pk__gt': 0};
// 1. Single Fetch
// fetch(filter, (response) => {
//   console.log(response);
// });

// !Long polling
var timeInterval = 1000;
// var timer1;
// function fetchLoop1() {
//     timer1 = setTimeout(function() {
//         fetch(filter, (response) => {
//           console.log(response);
//         });
//     }, timeInterval);
// }
// fetchLoop1();

// !Long polling with penalty
// var timer2;
// function fetchLoop2() {
//     timer2 = setTimeout(function() {
//         fetch(filter, (response) => {
//           console.log(response);
//           if (response.objects.length === 0) {
//               timeInterval += 1000;
//           }
//              console.log(timeInterval);
//              clearTimeout(timer2);
//              fetchLoop2();
//         });
//     }, timeInterval);
// }
// fetchLoop2();

// !Long polling with penalty with interval boundaries
var timer3;
var maxInterval = 5000;
var minInterval = 1000;
function fetchLoop() {
    timer3 = setTimeout(function() {
        fetch(filter, (response) => {
          console.log(response);
          if (response.objects.length === 0) {
              timeInterval += 1000;
          }
          if (timeInterval > maxInterval) {
              timeInterval = minInterval;
          }
          console.log(timeInterval);
          clearTimeout(timer3);
          fetchLoop();
        });
    }, timeInterval);
}
fetchLoop();
