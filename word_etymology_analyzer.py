
import os
import json
from datetime import datetime
import traceback
import glob
import re
import json5
import csv
from pprint import pprint
from openai import OpenAI

class JSONParsingError(Exception):
    def __init__(self, message, json_string, text):
        super().__init__(message)
        self.message = message
        self.json_string = json_string
        self.text = text


class WordEtymologyAnalyzer:
    def __init__(self, use_cache=True, max_retries=3):
        self.client = OpenAI()
        self.max_retries = max_retries
        self.analysis_folder = 'word_etymology_analysis'
        self.processed_log = 'processed_words.csv'
        self.ensure_folder_exists(self.analysis_folder)
        self.ensure_processed_log_exists()
        self.use_cache = use_cache
        
        
    def ensure_processed_log_exists(self):
        if not os.path.exists(self.processed_log):
            with open(self.processed_log, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['word', 'file_path'])

    def ensure_folder_exists(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def get_filename(self, word):
        datetime_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        return f"{self.analysis_folder}/{word}-{datetime_str}.json"

    def save_analysis(self, word, prompt, ai_response, filename):
        # filename = self.get_filename(word)
        data_to_save = {
            "word": word,
            "prompt": prompt,
            "response": ai_response
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)

    def load_latest_analysis(self, word):
        pattern = f"{self.analysis_folder}/{word}-*.json"
        files = glob.glob(pattern)
        if not files:
            return None  # No cache available

        latest_file = max(files, key=os.path.getctime)
        with open(latest_file, 'r', encoding='utf-8') as file:
            cached_data = json.load(file)
        return cached_data["response"]
    
    def extract_and_parse_json(self, text):
        bracket_pattern = r'\{.*\}'
        matches = re.findall(bracket_pattern, text, re.DOTALL)

        if not matches:
            raise JSONParsingError("No JSON string found in text", text, text)

        json_string = matches[0].replace('\n', '')
        try:
            parsed_json = json5.loads(json_string)
            if len(parsed_json) == 0:
                raise JSONParsingError("Parsed JSON string is empty", json_string, text)
            return parsed_json
        except ValueError as e:
            traceback.print_exc()
            raise JSONParsingError(f"JSON Decode Error: {e}", json_string, text)
            
            
    def check_processed(self, word):
        print(word)
        with open(self.processed_log, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                if row['word'] == word:
                    return row['file_path']
        return None

    def record_processed_word(self, word, file_path):
        # Check if the file exists and if it's empty
        file_exists = os.path.isfile(self.processed_log)
        need_header = not file_exists or os.stat(self.processed_log).st_size == 0

        with open(self.processed_log, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write header if needed
            if need_header:
                writer.writerow(['word', 'file_path'])
            
            # Then, write the word and file path
            writer.writerow([word, file_path])
    
            
            
    def analyze_word_etymology(self, word):
        retries = 0
        ai_response = None
        
        if self.use_cache:
            # cached_file_path = self.check_processed(word)
            # print("cached_file_path: ", cached_file_path)
            # if cached_file_path:
            #     with open(cached_file_path, 'r', encoding='utf-8') as file:
            #         return json.load(file)["response"]
            
            result =  self.load_latest_analysis(word)
            if result:
                return result
        
        messages = [
            {"role": "system", "content": "You are a linguistic expert analyzing words."},
            {"role": "user", "content": ""}
        ]

        while retries < self.max_retries:
            try:

                prompt = (
                    f"Conduct a comprehensive analysis of the word '{word}', starting with its meaning, example_words, language, "
                    "synonyms in Japanese, Arabic, French and Chinese, and provide an overview of its etymology. Dissect the word "
                    "to identify any prefixes, roots, and suffixes it may contain. For the etymology of each identified part, provide "
                    "meaning, example_words, the language of origin, a history and tracing and further etymology.\n\n"
                    "Delve deeper by RECURSIVELY (to the extreme, try your best, at least 3) tracing the origins of these components "
                    "to the extreme, ensuring to document the lineage of each part back to its absolute roots. Should any intermediate "
                    "root have a multifaceted history, illuminate the various branches of its evolution. Present this information in a "
                    "structured JSON format, adhering to the following template:\n\n"
                    "Use ``` to indicates start and end, if not finished yet don't use it.Output only JSON:\n"
                    "```json\n"
                    "{\n"
                    f"  \"word\": \"{word}\",\n"
                    "  \"meaning\": \"\",\n"
                    "  \"synonyms_in_other_languages\": {\"japanese\": \"\", \"arabic\": \"\", \"french\": \"\", \"chinese\": \"\"},\n"
                    "  \"language\": \"\",\n"
                    "  \"tracing\": [],\n"
                    "  \"history\": \"<Insert historical overview here>\",\n"
                    "  \"parts\": [\n"
                    "    {\n"
                    "      \"part\": \"<Name of part>\",\n"
                    "      \"type\": \"<Type: prefix/root/suffix>\"\n"
                    "    }\n"
                    "  ],\n"
                    "  \"etymology\": [\n"
                    "    {\n"
                    "      \"part\": \"<Name of part>\",\n"
                    "      \"meaning\": \"<Meaning of the part>\",\n"
                    "      \"example_words\": [],\n"
                    "      \"language\": \"<Language of origin>\",\n"
                    "      \"history\": \"<Historical background of the part>\",\n"
                    "      \"tracing\": [\"<Detailed tracing of etymology: xxx <-- yyy <-- zzz <-- www ...>\", \"xxx <-- bbb <-- ccc <-- ddd...\"]"
                    ",\n"
                    "      \"etymology\": [\n"
                    "        {\n"
                    "          \"part\": \"<Sub-part name>\",\n"
                    "          \"meaning\": \"<Meaning>\",\n"
                    "          \"language\": \"<Language>\",\n"
                    "          \"history\": \"<Historical background>\",\n"
                    "          \"example_words\": [],\n"
                    "          \"tracing\": [\"<Further tracing: yyy <-- zzz <-- www ...>\", \"yyy <-- ggg <-- hhh ...>\"]"
                    ",\n"
                    "          \"etymology\": [\n"
                    "            {\n"
                    "              \"part\": \"<Sub-sub-part name>\"\n"
                    "              ...\n"
                    "              \"etymology\": [\n"
                    "                  ...\n"
                    "              ]\n"
                    "            }\n"
                    "            ...\n"
                    "          ]\n"
                    "        }\n"
                    "      ]\n"
                    "    }\n"
                    "    ...\n"
                    "  ]\n"
                    "}\n"
                    "```"
                )

                messages[1]["content"] = prompt
                

                print(f"Querying OpenAI for the word '{word}' ...")

                response = self.client.chat.completions.create(
                    model=os.environ.get("OPENAI_MODEL", "gpt-4-0125-preview"),
                    messages=messages
                )

                ai_response = response.choices[0].message.content.strip()

                etymology_json = self.extract_and_parse_json(ai_response)




                filename = self.get_filename(word)
                self.save_analysis(word, prompt, etymology_json, filename)

                self.record_processed_word(word, filename)

                return etymology_json

            except (JSONParsingError, Exception) as e:
                print(f"Attempt {retries + 1} failed: {e}")
                messages.append({"role": "system", "content": str(ai_response)})
                messages.append({"role": "user", "content": str(e.message)})
                retries += 1
                if retries >= self.max_retries:
                    raise Exception("Reached maximum retries without success.")

        raise Exception("Reached maximum retries without success.")

if __name__ == "__main__":
    # This is a placeholder for how you would initialize and use the OpenAI client
    openai_client = None  # Make sure to instantiate your OpenAI client properly
    analyzer = WordEtymologyAnalyzer(use_cache=True)

    word = "etymology"
    analysis_result = analyzer.analyze_word_etymology(word)
    pprint(analysis_result)
