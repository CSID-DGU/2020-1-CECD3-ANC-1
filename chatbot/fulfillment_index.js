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

  const queryText = request.body.queryResult.queryText; // 사용자 입력문자 가져오기
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
  
  // 디비에 미해결 질문 저장
  function insertIntoDatabase(connection, data){
    return new Promise((resolve, reject) => {
      // 테이블 이름 변경
      connection.query('INSERT INTO question SET ? ', data, (error, results) => {
        resolve(results);
      });
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
    check = "더 자세한 내용은 1단원 교안 8 ~ 13 페이지를 참고하세요";
    if(parameter.compiler[0] == "compiler" && parameter.compiler[1] == "cross-compiler" && parameter.different == "차이점"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기고, 크로스 컴파일러는 소스 프로그램을 다른 기종에 대한 기계어로 번역하는 컴파일러입니다.";
    } else if(parameter.compiler == "compiler" && parameter.interpreter == "interpreter" && parameter.different == "차이점"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기고, 인터프리터는 고급언어로 작성된 코드를 한 단계씩 해설해서 실행시키는 방법입니다.";
    } else if(parameter.compiler == "compiler" && parameter.structure == "structure"){
      answer = "일반적인 컴파일러 구조는 \"어휘 분석기 (토큰)> 구문 분석기(트리) > 중간 코드 생성기(중간 코드) > 코드 최적화(최적화된 코드) > 타겟 코드 생성기\" 입니다. 그림과 ";
    } else if(parameter.compiler == "compiler"){
        answer = "컴파일러는 고급언어로 쓰인 프로그램을 컴퓨터에서 바로 실행될 수 있는 형태의 목적 프로그램으로 바꾸어 주는 번역기입니다.";
    } else if(parameter.interpreter == "interpreter"){
        answer = "인터프리터는 고급언어로 작성된 코드를 한 단계씩 해설해서 실행시키는 방법입니다.";
    } else if(parameter.preprocessor == "preprocessor"){
      answer = "프리프로세서, 즉 전처리기는 소스 프로그램을 확장된 소스 프로그램으로 바꿔줍니다. 이를 translator에서 target 프로그램으로 바꾸는 것입니다.";
  }
    agent.add(answer+check);
  }

  // 컴파일러 구조
  function handleCH1_CS(agent){
    var answer;
    if(parameter.structure == "lexical"){
      answer = "Lexical Analyzer, 즉 어휘 분석기는 컴파일러 내부에서 효율적이고 다루기 쉬운 정수로 바꾸어 줍니다. 1단원 교안 14 페이지를 참고하세요.";
    } else if(parameter.structure == "syntax"){
      answer = "Syntax Analyzer, 즉 구문 분석기는 구문을 확인하고 트리를 생성을 합니다. 1단원 교안 15 페이지를 참고하세요.";
    } else if(parameter.structure == "intermediate_code"){
      answer = "Intermediate Code Generator, 즉 중간 코드 생성기는 중간 코드를 생성합니다. 1단원 교안 16 페이지를 참고하세요.";
    } else if(parameter.structure == "optimizer"){
      answer = "Code Optimizer, 즉 코드 최적기는 비효율적인 코드를 구분해 효율적으로 바꾸어 줍니다. 최적화의 뜻, 기준, 지역 최적화, 전역 최적화도 공부해 보세요. 1단원 교안 17~18 페이지를 참고하세요.";
    } else if(parameter.structure == "target_code"){
      answer = "Target Code Generator, 즉 중간 코드 생성기는 중간 코드로부터 타겟 코드를 생성합니다. 1단원 교안 19 페이지를 참고하세요.";
    } else if(parameter.structure == "error"){
      answer = "Error recovery는 오류를 수정하는 것이고 Error repair는 오류가 발생하면 복구해 주는 것입니다. Error Handling의 종류와 Error의 종류는 1단원 교안 20 페이지를 참고하세요.";
    }
    agent.add(answer);
  }

  //컴파일러 자동화 도구
  function handleCH1_CGT(agent){
    var answer;
    if(parameter.CGT == "cgt"){
      answer = "컴파일러 자동화 도구는 compiler-compiler, Translator Writing System 이라고도 합니다. 1단원 교안 21 페이지를 참고하세요.";
    } else if(parameter.CGT == "lexical_ag"){
      answer = "Lexical Analyzer Generator, 즉 어휘 분석기 생성기는 정규표현으로 기술된 토큰들을 찾아내는 프로그램을 작성하는데 유용한 도구입니다. 1단원 교안 23 페이지를 참고하세요.";
    } else if(parameter.CGT == "parser_g"){
      answer = "Parser Generator, 즉 PGS는 Stanford PGS, Wisconsin PGS, YACC이 있습니다. 1단원 교안 24 페이지를 참고하세요.";
    } else if(parameter.CGT == "acg"){
      answer = "Automatic Code Generation은 1단원 교안 26 페이지를 참고하세요.";
    } else if(parameter.CGT == "ccs"){
      answer = "Compiler Compiler System은 PQCC와 ACK가 있습니다. 1단원 교안 27 페이지를 참고하세요.";
    } else if(parameter.model == "cc_model"){
      answer = "Compiler Compiler Model 구조는 1단원 교안 22 페이지를 참고하세요.";
    } else if(parameter.model == "pqcc_model"){
      answer = "PQCC Model 구조는 1단원 교안 28 페이지를 참고하세요.";
    } else if(parameter.model == "ack_model"){
      answer = "ACK Model 구조는 1단원 교안 29 페이지를 참고하세요.";
    }
    agent.add(answer);
  }

  // 미해결질문 등록
  // subject도 같이 등록할 수 있도록 수정
  function handleregi_question_custom(agent){
      const data = {
        q_c_name: parameter.subject,
        question: parameter.question,
        answer: "대기중"
      };
      return connectToDatabase().then(connection => {
        return insertIntoDatabase(connection, data).then(result => {
          agent.add( `강의명: ${parameter.subject} \n 질문: ${parameter.question} \n 을 등록합니다.`);

        });
      });
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
  intentMap.set('CH1_CS', handleCH1_CS);
  intentMap.set('CH1_CGT', handleCH1_CGT);
  intentMap.set('regi_question-custom', handleregi_question_custom);
  agent.handleRequest(intentMap);
	});

  