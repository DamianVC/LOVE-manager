Search.setIndex({docnames:["apidoc/api","apidoc/api.tests","apidoc/manage","apidoc/manager","apidoc/modules","apidoc/subscription","index","modules/how_it_works","modules/how_to_use_it","modules/overview","modules/readme_link"],envversion:{"sphinx.domains.c":1,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":1,"sphinx.domains.javascript":1,"sphinx.domains.math":2,"sphinx.domains.python":1,"sphinx.domains.rst":1,"sphinx.domains.std":1,"sphinx.ext.intersphinx":1,sphinx:56},filenames:["apidoc/api.rst","apidoc/api.tests.rst","apidoc/manage.rst","apidoc/manager.rst","apidoc/modules.rst","apidoc/subscription.rst","index.rst","modules/how_it_works.rst","modules/how_to_use_it.rst","modules/overview.rst","modules/readme_link.rst"],objects:{"":{api:[0,0,0,"-"],manage:[2,0,0,"-"],manager:[3,0,0,"-"],subscription:[5,0,0,"-"]},"api.apps":{ApiConfig:[0,1,1,""]},"api.apps.ApiConfig":{name:[0,2,1,""]},"api.authentication":{ExpiringTokenAuthentication:[0,1,1,""],TokenAuthentication:[0,1,1,""]},"api.authentication.ExpiringTokenAuthentication":{authenticate_credentials:[0,3,1,""],expires_in:[0,3,1,""],is_token_expired:[0,3,1,""],model:[0,2,1,""],token_expire_handler:[0,3,1,""]},"api.authentication.TokenAuthentication":{model:[0,2,1,""]},"api.middleware":{GetTokenMiddleware:[0,1,1,""]},"api.models":{GlobalPermissions:[0,1,1,""],Token:[0,1,1,""]},"api.models.GlobalPermissions":{DoesNotExist:[0,4,1,""],MultipleObjectsReturned:[0,4,1,""],id:[0,2,1,""],objects:[0,2,1,""]},"api.models.Token":{DoesNotExist:[0,4,1,""],MultipleObjectsReturned:[0,4,1,""],get_next_by_created:[0,3,1,""],get_previous_by_created:[0,3,1,""],id:[0,2,1,""],objects:[0,2,1,""],user:[0,2,1,""]},"api.serializers":{UserSerializer:[0,1,1,""]},"api.serializers.UserSerializer":{Meta:[0,1,1,""]},"api.serializers.UserSerializer.Meta":{fields:[0,2,1,""],model:[0,2,1,""]},"api.tests":{tests_auth_api:[1,0,0,"-"]},"api.tests.tests_auth_api":{AuthApiTestCase:[1,1,1,""]},"api.tests.tests_auth_api.AuthApiTestCase":{setUp:[1,3,1,""],test_user_fails_to_validate_deleted_token:[1,3,1,""],test_user_fails_to_validate_expired_token:[1,3,1,""],test_user_login:[1,3,1,""],test_user_login_failed:[1,3,1,""],test_user_login_twice:[1,3,1,""],test_user_logout:[1,3,1,""],test_user_validate_token:[1,3,1,""],test_user_validate_token_fail:[1,3,1,""]},"api.urls":{path:[0,5,1,""]},"api.views":{CustomObtainAuthToken:[0,1,1,""],logout:[0,5,1,""],validate_token:[0,5,1,""]},"api.views.CustomObtainAuthToken":{post:[0,3,1,""]},"manager.urls":{path:[3,5,1,""]},"subscription.auth":{TokenAuthMiddleware:[5,1,1,""]},"subscription.consumers":{SubscriptionConsumer:[5,1,1,""]},"subscription.consumers.SubscriptionConsumer":{connect:[5,3,1,""],disconnect:[5,3,1,""],handle_data_message:[5,3,1,""],handle_subscription_message:[5,3,1,""],receive_json:[5,3,1,""],subscription_ack:[5,3,1,""],subscription_all_data:[5,3,1,""],subscription_data:[5,3,1,""]},api:{admin:[0,0,0,"-"],apps:[0,0,0,"-"],authentication:[0,0,0,"-"],middleware:[0,0,0,"-"],models:[0,0,0,"-"],serializers:[0,0,0,"-"],tests:[1,0,0,"-"],urls:[0,0,0,"-"],views:[0,0,0,"-"]},manager:{asgi:[3,0,0,"-"],routing:[3,0,0,"-"],settings:[3,0,0,"-"],urls:[3,0,0,"-"],wsgi:[3,0,0,"-"]},subscription:{auth:[5,0,0,"-"],consumers:[5,0,0,"-"],routing:[5,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","attribute","Python attribute"],"3":["py","method","Python method"],"4":["py","exception","Python exception"],"5":["py","function","Python function"]},objtypes:{"0":"py:module","1":"py:class","2":"py:attribute","3":"py:method","4":"py:exception","5":"py:function"},terms:{"boolean":0,"case":7,"class":[0,1,3,5],"default":[7,10],"function":[0,3],"import":[0,3],"int":0,"new":8,"return":[0,8],"true":[0,8],"while":7,And:0,For:[0,3,7,9],The:[0,3,5,7,8,9,10],Then:7,These:[4,7],Use:[0,6],abov:7,access:[7,9],ack:5,acknowledg:[8,9],act:[7,10],action:7,add:[0,3],additt:0,admin:[3,4,10],admin_user_pass:10,alia:0,all:[5,7,9,10],also:[7,9],ani:9,anoth:[0,3],api:[4,6,8,9],apiconfig:0,apidoc:[6,7],app:[4,7],app_modul:0,app_nam:0,appconfig:0,append:8,appli:7,applic:[2,3,5,7,8,10],arg:[0,5],argument:0,as_view:[0,3],asgi:4,asgi_appl:3,associ:5,async:5,asynchron:8,asyncjsonwebsocketconsum:5,auth:[0,4],auth_ldap_server_uri:10,authapitestcas:1,authent:[1,4,5,6,7,9,10],authenticate_credenti:0,authenticationfail:0,author:[0,8,9],authtoken:0,avail:0,back:9,base:[0,1,3,5,8,9],bash:10,basic:7,becaus:7,been:0,befor:[0,10],behind:8,below:7,between:9,blog:[0,3],both:9,call:5,callabl:3,can:[0,1,7,10],cannot:[1,10],categori:[5,8],channel:[3,5,9,10],character:8,charg:7,check:[0,9],classmethod:0,client:[7,8,9],close_cod:5,cmd:[5,8,10],cmd_user_pass:10,code:[0,6,10],com:[0,3],command:[5,9,10],commandpath:[5,8],commun:[7,9],compar:7,compon:7,compos:[7,10],config:[0,3],configur:[0,3,7,10],confirm:8,connect:[5,6,7,9,10],consum:[4,8,9],contain:[0,5,7,10],content:[4,6,8],contrib:0,copi:10,core:0,correspond:[0,5,7,10],could:8,creat:[0,7],create_doc:10,credenti:[1,7,8,9],csc:[5,8],currenlti:0,current:[0,7,8],custom:[0,5],customobtainauthtoken:0,data1:8,data2:8,data:[0,5,7,8,9],databas:[0,7],datetimefield:0,defer:0,defin:[0,1,3,5,7,10],delet:[0,1,8],deploy:[3,10],deprec:10,describ:8,detail:[7,8,9],dev:7,develop:[6,7],dict:[0,5],dictionari:[0,5],differ:[1,7,8,9],disconnect:5,divid:7,django:[0,1,2,3,5,7,9,10],djangoproject:[0,3],djangpo:0,doc:[0,3],docker:7,docsrc:10,doe:10,doesnotexist:0,done:[7,8],drf:[0,9],each:[0,1,7,8],edit:10,email:0,empti:[0,10],end:8,endpoint:[0,7],entrypoint:3,env:10,environ:9,error:7,establish:[7,8,9,10],etc:7,event:[5,9],everi:[7,9,10],exampl:[4,6],except:0,exec:10,execut:[0,2,7,10],execute_command:8,expect:[5,8],expir:[0,1],expires_in:0,expiringtokenauthent:0,explain:7,expos:[0,3],fail:[0,1],fals:[0,8],field:0,figur:[7,9],file:[3,6,7],first:0,folder:10,follow:[5,7,8,9,10],foreignkei:0,format:[0,5],forward:[7,9],framework:9,from:[0,3,5,7,8,10],frontend:[7,9,10],full:3,further:9,gener:[0,3,5],get:8,get_next_by_cr:0,get_previous_by_cr:0,get_respons:0,gettokenmiddlewar:0,github:10,given:[0,7,8],globalpermiss:0,group:[5,6,7,9],handl:[0,5,7,9],handle_data_messag:5,handle_subscription_messag:5,handler:7,has:[0,7,9,10],have:[0,5,8,9],header:8,here:10,home:[0,3],host:10,how:[6,9],howto:3,html:10,http:[0,3,7,8,10],identifi:8,imag:7,implement:[7,10],includ:[0,3,9],incom:5,index:[0,6,10],inform:[0,3],ini:7,initi:7,inner:5,insid:[7,10],instanc:[0,5,7,8,9],instead:10,instruct:10,integr:10,intend:[5,8],interfac:0,intermediari:9,invalid:[0,1,7],is_next:0,is_token_expir:0,its:7,join:5,json:[0,5,8],kei:0,key1:8,key2:8,keyword:0,kwarg:[0,3,5],latter:[7,9],layer:10,ldap:10,leav:5,less:0,level:3,librari:7,list:[0,3],load:[0,6],local:6,locat:10,login:7,logout:[0,1],love:9,love_manager_redis_host:10,lsst:[9,10],mai:8,main:[2,7],make:[5,7],manag:[0,4,9,10],map:0,mechan:8,messag:[3,5,7,9],meta:0,methodnam:1,middlewar:[4,5,10],migrat:7,model:[4,7],modelseri:0,modul:[4,6,7],more:[0,3,7,9],mostli:7,mount:10,move:10,multipleobjectsreturn:0,must:[7,8,10],my_app:[0,3],name:[0,1,3,8],necessari:8,need:10,never:7,none:[0,3],number:[0,8],object:[0,5],objectdoesnotexist:0,obtain:0,obtainauthtoken:0,onc:[7,9,10],one:0,onli:[5,7],oper:[8,9],option:[5,8],order:[0,7,8,10],organ:6,other:[0,7,8],other_app:[0,3],otherwis:5,our:0,out:10,outsid:10,over:7,overview:6,packag:[4,6],page:[0,6],pair:8,param1:[5,8],param2:[5,8],param:[5,8],paramet:8,pars:5,part:[6,9],particular:[5,7,8,9],pass:8,password:[1,7,10],path:[0,3],pattern:[0,3],pend:5,permiss:[0,7,8,10],pipe:9,pleas:[0,3,7,9,10],post:[0,8],process_connection_pass:10,produc:[7,9,10],project:[0,3,4,9,10],provid:[0,7,8,9,10],purpos:[7,10],pytest:[7,10],python:[7,9],queri:0,rais:0,read:0,readm:6,readonli:10,reason:8,rebuild:10,receiv:[1,5,7,9],receive_json:5,recept:5,recommend:10,redi:10,redirect:9,redis_pass:10,ref:[0,3],refer:7,regist:0,reject:5,relat:0,remain:0,remian:0,remov:0,repli:[8,9],repo:10,repositori:10,repres:8,request:[0,1,7],requet:0,requier:7,requir:[7,8],resolv:[0,3],respect:7,respond:7,respons:[0,8],rest:[0,7,9],rest_framework:0,restart:10,rout:[0,4,7],routepattern:[0,3],rule:[3,5],run:[3,7],runserv:7,runtest:1,salindex:[5,8],script:7,scriptqueu:[5,8],search:[6,7],second:0,section:[7,9],see:[0,3,7,10],self:0,send:[5,7,9],sent:[8,9],serial:4,server:10,set:4,setup:1,shown:9,similarli:7,simpl:7,softwar:7,some:[7,10],sourc:8,specifi:8,sqlite3:7,src:10,stablish:8,startproject:[0,3],state:0,statu:[0,8],store:7,stream1:[5,8],stream2:5,stream:[5,8],string:0,submodul:4,subpackag:4,subscirpt:5,subscrib:[5,7,8,9],subscript:[4,6,7],subscription_ack:5,subscription_all_data:5,subscription_data:5,subscriptionconsum:5,succesfulli:8,success:8,suit:1,sure:7,system:[6,8],tel1:7,tel2:7,telemetri:[5,7,9],test:[0,4,7],test_user_fails_to_validate_deleted_token:1,test_user_fails_to_validate_expired_token:1,test_user_login:1,test_user_login_fail:1,test_user_login_twic:1,test_user_logout:1,test_user_validate_token:1,test_user_validate_token_fail:1,testcas:1,tests_auth_api:[0,4],than:0,thei:[0,8],them:8,therefor:9,thi:[0,3,7,8,9,10],thorugh:1,those:5,throgh:0,through:[7,8,9],time:[0,1],tio:10,token:[0,1,5,7,9],token_expire_handl:0,tokenauthent:0,tokenauthmiddlewar:5,tool:10,topic:[0,3],transfer:8,tri:7,trigger:8,turn:7,twie:1,txt:7,type:8,uniqu:7,unsubscrib:[5,8],unsubscript:5,unus:0,url:[4,7,8],urlconf:[0,3],urlpattern:[0,3],use:[0,5,6,10],used:[0,5,7,10],user:[0,1,5,7,10],user_data:8,user_user_pass:10,usernam:[0,7,8],userseri:0,uses:9,using:[0,1,3,9],usr:10,valid:[0,1,7],validate_token:0,valu:[0,3,7,8],value1:[5,8],value2:[5,8],variabl:[3,8],via:8,view:[3,4],visual:9,wai:[8,10],websocket:[3,5,6,7,9,10],when:[0,7,9],where:[8,9,10],which:[7,9,10],who:9,whole:3,work:[6,9],workflow:9,wrapper:0,written:9,wsgi:4,you:10},titles:["5.1. api package","5.1.1.1. api.tests package","5.2. manage module","5.3. manager package","5. ApiDoc","5.4. subscription package","Welcome to LOVE-manager\u2019s documentation!","3. How it works","2. How to use it","1. Overview","4. Readme File"],titleterms:{Use:10,accept:8,admin:0,api:[0,1,7],apidoc:4,app:0,asgi:3,auth:5,authent:[0,8],build:10,channel:7,code:7,command:8,connect:8,consum:[5,7],content:[0,1,3,5],develop:10,docker:10,document:[6,10],environ:10,event:8,exampl:[0,3,7],file:10,get:10,group:8,how:[7,8],imag:10,indic:6,initi:10,layer:7,load:10,local:10,logout:8,love:[6,7,8,10],manag:[2,3,6,7,8],messag:8,middlewar:0,model:0,modul:[0,1,2,3,5],organ:7,overview:9,packag:[0,1,3,5],part:[7,10],password:8,readm:10,request:8,rout:[3,5],run:10,scheme:8,serial:0,set:3,submodul:[0,1,3,5],subpackag:0,subscript:[5,8],system:10,tabl:6,telemetri:8,test:[1,10],tests_auth_api:1,token:8,url:[0,3],use:8,user:8,valid:8,variabl:10,view:0,websocket:8,welcom:6,work:7,wsgi:3}})