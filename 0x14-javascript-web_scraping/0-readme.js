#!/usr/bin/node
const fs = require('fs');
// const request = require('request');
const url = process.argv[2];
fs.readFile (url, 'utf-8', (error, data) => {
    if (error) {
        console.log(error);
        return;
    } 
    console.log(data);
    
});

