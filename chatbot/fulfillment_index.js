// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';
 
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const {WebhookClient} = require('dialogflow-fulfillment');
const {Card, Suggestion} = require('dialogflow-fulfillment');
const mysql = require('mysql');
//admin.initializeApp({
	//credentail: admin.credential.applicationDefault(),
  	//databaseURL: 'ws://kobaksa-1b59d.firebaseio.com/'
//});
process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements
 
exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });

  const parameter = request.body.queryResult.parameters; //쿼리 결과에서 파라미터 정보 가져오기

  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
 
  function welcome(agent) {
    agent.add(`안녕하세요. 난 고박사예요. 뭐 질문있나요?`);
  }
 
  function fallback(agent) {
    agent.add(`무슨 소린지 모르겠군요`);
    agent.add(`미안해요. 못 알아 들었어요. 다시 한번 말해줄래요?`);
  }
 function testconnDB(agent){
     return admin.database().ref().once('value').then((snapshot) => {
       let test = snapshot.child('testconnDB').val();
       agent.add(`db 연결 테스트..${test}`);
     });}
/* MySQL 연결 정보 */
function connectToDatabase(){
  const connection = mysql.createConnection({
  	host:'52.78.240.248',
    user:'moodle',
    password:'1234',
    database:'moodle'
  });
  
  return new Promise((resolve, reject) => {
    connection.connect();
    resolve(connection);
  });
}
  
  function queryDatabase(connection){
    return new Promise((resolve, reject)=>{
    	connection.query('SELECT * from users',(error, results, fields)=>{
          resolve(results);
        });
    });
  }
  
  function handleReadFromMySQL(agent){
  	return connectToDatabase().then(connection =>{
      return queryDatabase(connection).then(result => {
        console.log(result);
        agent.add(`Name: ${result[0].name}`);
        connection.end();
      });
    });
  }
  
  /* 1단원 */
  function handleCH1_PL(agent){
    var answer;
    if(parameter.PL == "COBOL" || parameter.PL == "cobol" || parameter.PL =="코볼"){
        answer = "COBOL은 1960년대 초 코다실(CODASYL)에서 발표한 COmmon Business Oriented Language 입니다. 더 자세한 내용은 1단원 교안 4 페이지를 참고하세요.";
    } else if(parameter.PL == "FORTRAN" || parameter.PL == "fortran" || parameter.PL == "포트란"){
        answer = "FORTRAN은 1977년 FORTRAN77이 발표한 FORmula TRANslation 입니다. 더 자세한 내용은 1단원 교안 4 페이지를 참고하세요.";
    } else if(parameter.PL == "ALGOL" || parameter.PL == "algol" || parameter.PL == "알골"){
        answer = "ALGOL은 1968년 IFIP WG2.1에서 발표한 ALGOrithmic Language 입니다. 더 자세한 내용은 1단원 교안 5 페이지를 참고하세요.";
    } else if(parameter.PL == "Pascal" || parameter.PL == "PASCAL" || parameter.PL == "파스칼"){
        answer = "Pascal은 1970년대 초, N.Wirth가 고안한 언어입니다. 더 자세한 내용은 1단원 교안 5 페이지를 참고하세요.";
    } else if(parameter.PL == "Ada" || parameter.PL == "ADA" || parameter.PL == "아다"){
        answer = "Ada은 1980년에 발표된 언어입니다. 더 자세한 내용은 1단원 교안 6 페이지를 참고하세요.";
    } else if(parameter.PL == "C++" || parameter.PL == "c++"){
      answer = "C++은 1983년에 발표된 언어입니다. 더 자세한 내용은 1단원 교안 6 페이지를 참고하세요.";
    } else if(parameter.PL == "Java" || parameter.PL == "java" || parameter.PL == "자바"){
      answer = "Java은 Sun MicroSystems에서 1995년에 개발한 객체 지향 프로그래밍 언어 입니다. 더 자세한 내용은 1단원 교안 7 페이지를 참고하세요.";
    } else if(parameter.PL == "C#" || parameter.PL == "c#" || parameter.PL == "씨샾"){
      answer = "C#은 Microsoft에서 개발한 객체지향 프로그래밍 언어입니다. 더 자세한 내용은 1단원 교안 7 페이지를 참고하세요.";
    } 
    agent.add(answer);
  }
  // Run the proper function handler based on the matched Dialogflow intent name
  let intentMap = new Map();
  intentMap.set('Default Welcome Intent', welcome);
  intentMap.set('Default Fallback Intent', fallback);
  // intentMap.set('your intent name here', yourFunctionHandler);
  // intentMap.set('your intent name here', googleAssistantHandler);
  intentMap.set('test', testconnDB);
  intentMap.set('getDataFromMySQL', handleReadFromMySQL);
  intentMap.set('CH1_PL', handleCH1_PL);
  agent.handleRequest(intentMap);
	});
