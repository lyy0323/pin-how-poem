# Pin-How-Poem

This project is a Python-based tool for generating Chinese poetry using a dice-rolling mechanism. It allows users to create poems by randomly selecting words based on predefined rules and tones (平/仄). The project is designed to simulate the creative process of poetry composition in a fun and interactive way.

## Features

- **Dice-based Word Selection**: Words are selected randomly from a predefined bank of words using dice objects. This predefined word bank is a collaborative work of members in Wenyun Department, Guoxue Club, SJTU.
- **Tone Rules**: Supports tone rules (平/仄) for Chinese poetry.
- **Customizable Rules**: Users can define their own rhyme schemes for word selection. The default rhyme scheme is `[("double", "ze"), ("double", "ping"), ("single", "ping"), ("double", "ze")`, which stands for "仄仄平平平仄仄，平平仄仄仄平平", a common rhyme scheme of traditional 7-syllable verses.
- **Batch Experiments**: Generate multiple poems with customizable draw and roll counts.
- **Save Results**: Option to save generated poems and their attributes to a file.

## Project Structure

- **`roll.py`**: Main script containing the implementation of the dice and dice bank, as well as the experiment logic.
- **`bank.txt`**: Word bank file containing the words used for poem generation.
- **`save.txt`**: File where generated poems and their attributes are saved.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/pin-how-poem.git
    cd pin-how-poem
    ```

2. Ensure you have Python 3 installed.

## Usage

1. Prepare the word bank file (bank.txt) with the following format(This should be already predefined, but feel free to define your own):

    ```plaintext
    1. word1 ... word6 | word7 ... word12
    2. word13 ...  word18 | word19 ... word24
    ...
    ```

    Each line represents a pair of words with their tones (平/仄).

2. Run the script:

    ```shell
    python roll.py
    ```

3. You can customize the rules and experiment parameters in the `__main__` section of roll.py:

    - rule: Define the structure of the poem (e.g., word length and tone).
    - draws: Number of times to draw a sample.
    - rolls: Number of times to roll the dice for each sample.
    - save: Whether to save the results to `save.txt`.
    - save_attr: Whether to save the attributes of the dice used.

4. View the generated poems in the terminal or in the `save.txt` file.

## Example Output

```plaintext
鸟迹空梁留彩笔，花香古渡见朱楼。
```

## Customization

- Modify the `bank.txt` file to include your own words.
- Adjust the rules in the experiment function to create different poem structures.
- Adjust number of draws and rolls of each draw in an experiment.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to the creators of the word bank and the inspiration behind this project.

- The inspiration is put forward by [lyy0323(林雨夜/芋椰)](https://github.com/lyy0323/) during her chat with 萌萌(长安).
- The word bank is created by collaborative work of members in Wenyun Department, Guoxue Club, SJTU.
- This project has an off-line version with REAL WOODEN DICES and a rule board. Contact Guoxue Club, SJTU to have access to the cute dices :)
