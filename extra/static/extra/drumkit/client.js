const notes = {
    a: 'clap',
    s: 'hihat',
    d: 'kick',
    f: 'openhat',
    g: 'boom',
    h: 'ride',
    j: 'snare',
    k: 'tom',
    l: 'tink'
};
const csrftoken = $('[name=csrfmiddlewaretoken]').val();

function sendEvent(e) {
    if (!notes.hasOwnProperty(e.key)) {
        return;
    }
    $.ajax({
        type: 'POST',
        url: '/drumkit/',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        data: {note: notes[e.key]}
    });
}

window.addEventListener('keydown', sendEvent);
