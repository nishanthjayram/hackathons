
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').addEventListener('click', function () {
        chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function (tabs) {
            let url = tabs[0].url;
            if (url.startsWith('https://www.linkedin.com/jobs/view'))
            {
                firebase.database().ref('url/').set('url', url);
            }
        })
    })
})