import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def line_plot(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x_col, y=y_col)
    plt.title(f'Line Plot of {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def bar_plot(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(f'Bar Plot of {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def scatter_plot(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.title(f'Scatter Plot of {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def histogram(df, col):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=col, kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

def heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Heatmap of Correlation Matrix')
    plt.show()

def interactive_scatter_plot(df, x_col, y_col, color_col=None):
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col,
                    title=f'Interactive Scatter Plot of {y_col} vs {x_col}')
    fig.show()

def menu():
    print("Data Visualizer Menu:")
    print("1. Load Data")
    print("2. Line Plot")
    print("3. Bar Plot")
    print("4. Scatter Plot")
    print("5. Histogram")
    print("6. Heatmap")
    print("7. Interactive Scatter Plot")
    print("8. Exit")

    return int(input("Choose an option (1-8): "))

if __name__ == "__main__":
    df = None
    while True:
        choice = menu()
        
        if choice == 1:
            file_path = input("Enter the CSV file path: ")
            df = load_data(file_path)
        
        elif choice in [2, 3, 4, 5, 6, 7] and df is None:
            print("Please load data first.")
        
        elif choice == 2:
            x_col = input("Enter the x-axis column name: ")
            y_col = input("Enter the y-axis column name: ")
            line_plot(df, x_col, y_col)
        
        elif choice == 3:
            x_col = input("Enter the x-axis column name: ")
            y_col = input("Enter the y-axis column name: ")
            bar_plot(df, x_col, y_col)
        
        elif choice == 4:
            x_col = input("Enter the x-axis column name: ")
            y_col = input("Enter the y-axis column name: ")
            scatter_plot(df, x_col, y_col)
        
        elif choice == 5:
            col = input("Enter the column name for histogram: ")
            histogram(df, col)
        
        elif choice == 6:
            heatmap(df)
        
        elif choice == 7:
            x_col = input("Enter the x-axis column name: ")
            y_col = input("Enter the y-axis column name: ")
            color_col = input("Enter the color column name (or press Enter to skip): ")
            color_col = color_col if color_col else None
            interactive_scatter_plot(df, x_col, y_col, color_col)
        
        elif choice == 8:
            print("Exiting Data Visualizer.")
            break
        
        else:
            print("Invalid choice. Please try again.")