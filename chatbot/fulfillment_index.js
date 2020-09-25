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
  // 프로그래밍 언어 종류
  function handleCH1_PL(agent){
    var answer;
    if(parameter.pl == "COBOL"){
        answer = "COBOL은 1960년대 초 코다실(CODASYL)에서 발표한 COmmon Business Oriented Language 입니다. 더 자세한 내용은 1단원 교안 4 페이지를 참고하세요.";
    } else if(parameter.pl == "FORTRAN"){
        answer = "FORTRAN은 1977년 FORTRAN77이 발표한 FORmula TRANslation 입니다. 더 자세한 내용은 1단원 교안 4 페이지를 참고하세요.";
    } else if(parameter.pl == "ALGOL"){
        answer = "ALGOL은 1968년 IFIP WG2.1에서 발표한 ALGOrithmic Language 입니다. 더 자세한 내용은 1단원 교안 5 페이지를 참고하세요.";
    } else if(parameter.pl == "Pascal"){
        answer = "Pascal은 1970년대 초, N.Wirth가 고안한 언어입니다. 더 자세한 내용은 1단원 교안 5 페이지를 참고하세요.";
    } else if(parameter.pl == "Ada"){
        answer = "Ada은 1980년에 발표된 언어입니다. 더 자세한 내용은 1단원 교안 6 페이지를 참고하세요.";
    } else if(parameter.pl == "C++"){
      answer = "C++은 1983년에 발표된 언어입니다. 더 자세한 내용은 1단원 교안 6 페이지를 참고하세요.";
    } else if(parameter.pl == "Java"){
      answer = "Java은 Sun MicroSystems에서 1995년에 개발한 객체 지향 프로그래밍 언어 입니다. 더 자세한 내용은 1단원 교안 7 페이지를 참고하세요.";
    } else if(parameter.pl == "C#"){
      answer = "C#은 Microsoft에서 개발한 객체지향 프로그래밍 언어입니다. 더 자세한 내용은 1단원 교안 7 페이지를 참고하세요.";
    } 
    agent.add(answer);
  }

  // 번역기와 컴파일러
  function handleCH1_IC(agent){
    var answer; var check;
    check = "더 자세한 내용은 1단원 교안 8 ~ 12 페이지를 참고하세요";
    if(parameter.compiler[0] == "compiler" && parameter.compiler[1] == "cross-compiler" && parameter.different == "차이점"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기고, 크로스 컴파일러는 소스 프로그램을 다른 기종에 대한 기계어로 번역하는 컴파일러입니다.";
    } else if(parameter.compiler == "compiler" && parameter.interpreter == "interpreter" && parameter.different == "차이점"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기고, 인터프리터는 고급언어로 작성된 코드를 한 단계씩 해설해서 실행시키는 방법입니다.";
    } else if(parameter.compiler == "compiler"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기입니다.";
    } else if(parameter.interpreter == "interpreter"){
        answer = "인터프리터는 고급언어로 작성된 코드를 한 단계씩 해설해서 실행시키는 방법입니다.";
    }
    agent.add(answer+check);
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
  intentMap.set('CH1_IC', handleCH1_IC);
  agent.handleRequest(intentMap);
	});
