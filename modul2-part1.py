 # 2. Iterate over the line input looking for non-zero entries. For each non-zero entry, put the value into the
    # next available entry of the result list (starting at position 0).
    if len(line) < 2:
        return line

    for entry_index in range(0, len(line)):
        if line[entry_index] != 0:
            # find the start point first
            for re_index in range(0, len(result)):
                # if it is 0 then can copy safely
                if result[re_index] == 0:
                    result[re_index] = line[entry_index]
                    last_merged = False
                    break
                # if current is not 0 but the next one is, then need to consider merge
                elif result[re_index + 1] == 0:
                    # current is the same with incoming one, merge
                    if result[re_index] == line[entry_index] and last_merged is False:
                        result[re_index] = result[re_index] + line[entry_index]
                        last_merged = True
                        break
                        # else advance to next iter
                        # if current is not 0 and the next one is not 0, advance to next iter

    return result

   