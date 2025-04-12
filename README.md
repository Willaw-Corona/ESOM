# ESOM

ESOM (Enhanced Self-Organizing Maps) is a Python-based tool designed for clustering and visualizing high-dimensional data. It provides an intuitive interface for exploring data patterns and relationships.

## Features

- **Data Clustering**: Automatically groups similar data points.
- **Visualization**: Generates 2D maps for high-dimensional data.
- **Customizable Parameters**: Adjust learning rates, grid sizes, and more.
- **Interactive Interface**: Explore results visually through the generated maps.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Cesar-Gabriel/ESOM.git
    ```
2. Navigate to the project directory:
    ```bash
    cd ESOM
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your dataset in a CSV format.
2. Run the ESOM script:
    ```bash
    python esom.py --input your_dataset.csv --output output_map.png
    ```
3. Open `index.html` in your browser to visualize the results.

### Command-Line Options

- `--input`: Path to the input dataset (CSV format).
- `--output`: Path to save the generated map image.
- `--grid-size`: Specify the grid size for the map (default: 10x10).
- `--learning-rate`: Set the learning rate for training (default: 0.1).

## Visualization

The `index.html` file provides an interactive visualization of the generated map. Open it in any modern web browser to explore the clusters and relationships in your data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their support.
 
