### 장고 개발
<!-- 
화면 1 (크롤링 사이트 등록 관리화면)
- mariadb에 크롤링 대상 SITE 테이블 생성
(URL_NAME, URL) -->



화면 2 ( 키워드 입력, 화면 1에서 등록된 리스트 중(URL_NAME) 에 선택, 버튼(  ) 기능  )
※ 목적 : 웹에서 크롤러 동작 확인을 위해

<!-- - 저장된 데이터 불러 올 수 있는 화면 필요(title 기준) -->
- Search box 검색( 자동완성 기능 )
- 예제: 네이버 일간지 (조선일보 타겟)


결론적으로 SITE 테이블 만들고, Keyword 테이블 만들기, 모듈 동작 확인까지 금
- 스케줄러 (시간 커스터마이징 기능 고민 )

- 키바나 하이퍼링크









DB 설계  ( url 끝에는  '/'을 붙이기 않는다.)  ※DB 테이블 명명 규칙 ( 기능 대분류 / 권한 / 기능 중분류 )


api_method
- 요청방법	method				VARCHAR
- 설명	discription			VARCHAR


api_response
- 응답값	response_code		INTEGER
- 설명	discription			VARCHAR


admin_custom_pattern
- 패턴	pattern				VARCHAR
- adm타겟	admin_target		INTEGER		(request_user_target key id 값)



user_custom_pattern
- 패턴	pattern				VARCHAR
- usr타겟	user_target			INTEGER		(request_user_target key id 값)



request_admin_custom_parse_result
- 결과	result				VARCHAR
- 패턴	admin_custom_pattern_id			INTEGER		(admin_custom_pattern key id 값)



request_user_custom_parse_result
- 결과	result				VARCHAR
- 패턴	user_custom_pattern_id			INTEGER		(user_custom_pattern key id 값)

request_result
- 종류	extension			VARCHAR


request_baseurl   
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 기본주소	baseurl				VARCHAR


request_suburl
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 서브주소	suburl				VARCHAR


request_header
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 헤더값	header				VARCHAR


request_param
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 요청값	param				VARCHAR




request_admin_target
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 기본주소	baseurl				INTEGER		(request_baseurl key id 값)
- 헤더값	header				INTEGER		(request_header key id 값)
- 서브주소	suburl				INTEGER		(request_suburl key id 값)
- 요청값	param				INTEGER		(request_param key id 값)



request_user_target
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 기본주소	baseurl				INTEGER		(request_baseurl key id 값)
- 헤더값	header				INTEGER		(request_header key id 값)
- 서브주소	suburl				INTEGER		(request_suburl key id 값)
- 요청값	param				INTEGER		(request_param key id 값)


request_admin_raw
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- adm타겟	admin_target		INTEGER		(request_admin_target key id 값)
- 종류	extension			INTEGER		(request_result key id 값)
- raw값	raw값				VARCHAR


request_user_raw
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- adm타겟	user_target			INTEGER		(request_user_target key id 값)
- 종류	extension			INTEGER		(request_result key id 값)
- raw값	raw값				VARCHAR


request_admin_target_log
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 타깃주소	admin_target		INTEGER		(request_admin_target key id 값)


request_user_target_log
- 접속자	access_user			INTEGER
- 등록일	enrolled_date 		DATETIME
- 수정일	edited_date			DATETIME
- 사용중	is_active			INTEGER
- 승인된	is_approved			INTEGER
- 타깃주소	user_target			INTEGER		(request_user_target key id 값)



execute_user_job_log

- 타깃주소 user_target			INTEGER		(request_user_target key id 값) 
- job상태   user_job_status              INTEGER        (0: 정지, 1:진행중, 2:완료)





execute_admin_job_log

- 타깃주소 admin_target		INTEGER		(request_admin_target key id 값)
- job상태   admin_job_status              INTEGER        (0: 정지, 1:진행중, 2:완료)