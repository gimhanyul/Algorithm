def identify_and_convert_variable_name(variable_name: str) -> str:
    if "_" in variable_name:  # 가능한 C++ 형식
        # C++ 형식 검증
        if variable_name.startswith("_") or variable_name.endswith("_") or "__" in variable_name or any(c.isupper() for c in variable_name):
            return "Error!"
        # C++ -> Java 변환
        parts = variable_name.split("_")
        return parts[0] + "".join(part.capitalize() for part in parts[1:])
    else:  # 가능한 Java 형식
        # Java 형식 검증
        if variable_name[0].isupper() or "_" in variable_name:
            return "Error!"
        # Java -> C++ 변환
        result = []
        for c in variable_name:
            if c.isupper():
                result.append("_" + c.lower())
            else:
                result.append(c)
        return "".join(result)

# 사용자 입력 예시
user_input_examples = input()

print(identify_and_convert_variable_name(user_input_examples))
