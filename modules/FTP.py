from ftplib import FTP
import os 

class TransFTP:
    def upload_files_to_ftp(self, ftp_server, ftp_user, ftp_password, file_paths, upload_dir):
        """
        여러 파일을 FTP 서버에 업로드
        :param ftp_server: FTP 서버 주소 (예: 'ftp.example.com')
        :param ftp_user: FTP 사용자명
        :param ftp_password: FTP 비밀번호
        :param file_paths: 업로드할 로컬 파일 경로 리스트
        :param upload_dir: FTP 서버의 업로드 디렉토리 경로
        """
        try:
            # FTP 연결
            ftp = FTP(ftp_server)
            ftp.login(user=ftp_user, passwd=ftp_password)
            print("FTP 연결 성공!")

            # 파일 전송
            for file_path in file_paths:
                try:
                    file_name = os.path.basename(file_path)  # 파일 이름 추출
                    upload_path = f"{upload_dir}/{file_name}"  # 업로드 경로 생성
                    with open(file_path, "rb") as file:
                        ftp.storbinary(f"STOR {upload_path}", file)
                    print(f"파일 업로드 성공: {file_name} -> {upload_path}")
                except Exception as file_error:
                    print(f"파일 업로드 중 오류 발생: {file_path}, 오류: {file_error}")

            # FTP 연결 종료
            ftp.quit()
            print("FTP 연결 종료.")
        except Exception as e:
            print(f"FTP 연결 중 오류 발생: {e}")