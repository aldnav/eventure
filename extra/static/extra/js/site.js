let filter = {'pk__gt': 0};
let timeInterval = 3000;
var timer3;
var maxInterval = 5000;
var minInterval = 1000;


/**
 * Fetch from stream
 * @param  {Object}   filter   filter to pass to API
 * @param  {Function} callback invoke on success
 */
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


/**
 * Continuous fetch
 */
function fetchLoop() {
    timer3 = setTimeout(function() {
        fetch(filter, (response) => {
          console.log(response.objects);
          if (response.objects.length === 0) {
              timeInterval += 1000;
          }
          if (timeInterval > maxInterval) {
              timeInterval = minInterval;
          }
          renderStream(response.objects);
          clearTimeout(timer3);
          fetchLoop();
        });
    }, timeInterval);
}
fetchLoop();

/**
 * Renders stream objects
 * @param  {Array} objects Stream objects
 */
const template = $('#activity-template').html();
function renderStream(objects) {
    for (let i = 0; i < objects.length; i++) {
        let object = objects[i];
        console.log(object);
        let rendered = Mustache.render(template, object);
        $('.activity-stream').prepend(rendered);
    }
}
