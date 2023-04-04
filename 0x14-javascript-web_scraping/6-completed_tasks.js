#!/usr/bin/node
// Returns user id and number of completed tasks

const req = require('request');
const ag = process.argv;

req(ag[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });
    console.log(completed);
  }
});
