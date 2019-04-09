import boto3
import os
 
def upload_files(path):
    # S3 리소스 객체 생성
    session = boto3.Session(
        aws_access_key_id='AKIAXZVQ7GX4HAYWWUON',
        aws_secret_access_key='***************',
        region_name='ap-northeast-2'
    )
    s3 = session.resource('s3')

    # 업로드할 S3 버킷이름 지정
    bucket_name = 'dstagram-django'
    
    # 로컬에 저장된 파일 검색
    for subdir, dirs, files in os.walk(path):
        for file in files:
            # print(subdir.replace('\\', '/'))
            # 윈도우 환경에서 실행한 경우, 경로 구분자를 변경해 준다.
            subdir = subdir.replace('\\', '/')
            # os.path.join() 을 사용하면 시스템 운영체제를 기준으로 경로를 생성하므로 문자열로 완성한다.
            full_path = subdir + '/' + file
            # print(full_path)

            # s3.meta.client.upload_file(로컬 파일명, 버킷 이름, 버킷에 저장될 파일명)
            s3.meta.client.upload_file(full_path, bucket_name, full_path)

 
if __name__ == "__main__":
    upload_files('media')