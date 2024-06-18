import ffmpeg
import os

def convert_vob_to_mp4(input_file, output_file):
    ffmpeg.input(input_file).output(output_file).run()

def convert_directory(input_dir, output_dir):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    for file in os.listdir(input_dir):
        if file.endswith('.VOB'):
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.mp4")
            print(f"Convertendo {input_file_path} para {output_file_path}")
            convert_vob_to_mp4(input_file_path, output_file_path)
            print(f"Arquivo {output_file_path} criado com sucesso.")

if __name__ == "__main__":
    input_directory = r"dir:diretorio\de_entrada"
    output_directory = r"dir:diretorio\de_saida"
    convert_directory(input_directory, output_directory)
