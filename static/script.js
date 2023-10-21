function sendHttpRequest(method, url, data) {
  return fetch(url, {
    method: method,
    body: data,
    headers: {
      'Authorization': `Basic ${base64Credentials}`,
    },
  })
    .then(response => {
      if (response.status === 200) {
        return response.text();
      } else if (response.status === 401) {
        return Promise.reject('Unauthorized');
      } else {
        return Promise.reject('Request failed');
      }
    });
}

document.getElementById('login-button').addEventListener('click', function () {
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;
  const credentials = `${username}:${password}`;
  const base64Credentials = btoa(credentials);

  sendHttpRequest('POST', '/login', null)
    .then(responseData => {
      alert('Login successful.');
    })
    .catch(error => {
      alert('Login failed. Invalid username or password.');
    });
});

document.getElementById('get-button').addEventListener('click', function () {
  const queryParameter = 'someQueryData';
  const url = `/get-route?data=${queryParameter}`;
  sendHttpRequest('GET', url, null)
    .then(responseData => {
      alert('GET request succeeded. Response: ' + responseData);
    })
    .catch(error => {
      alert('GET request failed. Error: ' + error);
    });
});

document.getElementById('put-button').addEventListener('click', function () {
  const queryParameter = 'someQueryData';
  const url = `/put-route?data=${queryParameter}`;
  const data = 'Data to send in PUT request';
  sendHttpRequest('PUT', url, data)
    .then(responseData => {
      alert('PUT request succeeded. Response: ' + responseData);
    })
    .catch(error => {
      alert('PUT request failed. Error: ' + error);
    });
});

document.getElementById('delete-button').addEventListener('click', function () {
  const queryParameter = 'someQueryData';
  const url = `/delete-route?data=${queryParameter}`;
  sendHttpRequest('DELETE', url, null)
    .then(responseData => {
      alert('DELETE request succeeded. Response: ' + responseData);
    })
    .catch(error => {
      alert('DELETE request failed. Error: ' + error);
    });
});