const http = require('http');
const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const url = require('url');
const json = require('json');

const server = http.createServer((req, res) => {
  const path = url.parse(req.url, true).pathname;
  
  if (req.method === 'GET') {
    if (path === '/') {
      fs.readFile('templates/index.html', 'utf8', (err, html) => {
        if (err) {
          res.statusCode = 404;
          res.end('Not Found');
        } else {
          res.statusCode = 200;
          res.setHeader('Content-type', 'text/html');
          res.end(html);
        }
      });
    } else if (path === '/database') {
      const db = new sqlite3.Database('database.sqlite');
      db.all('SELECT * FROM students', (err, rows) => {
        if (err) {
          res.statusCode = 500;
          res.setHeader('Content-type', 'application/json');
          res.end(JSON.stringify({ error: err }));
        } else {
          res.statusCode = 200;
          res.setHeader('Content-type', 'application/json');
          res.end(JSON.stringify({ database: rows }));
        }
      });
      db.close();
    }
  } else if (req.method === 'POST') {
    const body = [];
    req.on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
      const data = Buffer.concat(body).toString();
      const db = new sqlite3.Database('database.sqlite');
      db.run(`INSERT INTO students(name, contact_phone, contact_email, contact_address, application_date, application_status, program_course, test_scores, transcripts, recommendation_letters, application_fee_payment_status, application_essays, application_reviewer) VALUES(${data})`, (err) => {
        if (err) {
          res.statusCode = 500;
          res.setHeader('Content-type', 'application/json');
          res.end(JSON.stringify({ error: err }));
        } else {
          res.statusCode = 200;
          res.setHeader('Content-type', 'application/json');
          res.end(JSON.stringify({ message: 'Received POST data and inserted into the database.' }));
        }
      });
      db.close();
    });
  } else if (req.method === 'PUT') {
    const body = [];
    req.on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
      const data = Buffer.concat(body).toString();
      const id = path.split('/').pop();
      const db = new sqlite3.Database('database.sqlite');
      db.run(`UPDATE students SET name = ${data} WHERE id = ${id}`, (err) => {
        if (err) {
          res.statusCode = 500;
          res.setHeader('Content-type', 'application/json');
          res.end(JSON.stringify({ error: err }));
        } else {
          res.statusCode = 200;
          res.setHeader('Content-type', 'text/plain');
          res.end(`Updated student record with ID ${id} in the database`);
        }
      });
      db.close();
    });
  } else if (req.method === 'DELETE') {
    const id = path.split('/').pop();
    const db = new sqlite3.Database('database.sqlite');
    db.run(`DELETE FROM students WHERE id = ${id}`, (err) => {
      if (err) {
        res.statusCode = 500;
        res.setHeader('Content-type', 'application/json');
        res.end(JSON.stringify({ error: err }));
      } else {
        res.statusCode = 200;
        res.setHeader('Content-type', 'text/plain');
        res.end(`Deleted student record with ID ${id} from the database`);
      }
    });
    db.close();
  } else {
    res.statusCode = 400;
    res.setHeader('Content-type', 'text/plain');
    res.end('Bad Request');
  }
});

const port = process.env.PORT || 8080;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});