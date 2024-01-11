import os
import arxiv

def download_latex_sources(category, max_papers_per_category=100):
    # Create a directory to store downloaded LaTeX sources
    output_directory = f"{category}_papers"
    os.makedirs(output_directory, exist_ok=True)

    # Initialize the ArXiv client
    client = arxiv.Client()

    # Define the query parameters for the ArXiv API
    query_params = {
        'category': f'math.{category}',
        'max_results': max_papers_per_category,
        'sort_by': 'submittedDate',
        'sort_order': 'descending'
    }

    # Query the ArXiv API
    papers = client.results(arxiv.Search(**query_params))

    # Download LaTeX sources for each paper
    for i, paper in enumerate(papers):
        if i >= max_papers_per_category:
            break

        paper_id = paper.id.split('/')[-1]
        output_file_path = os.path.join(output_directory, f'{paper_id}.tar.gz')

        # Download the LaTeX source to the specified directory with a custom filename
        paper.download_source(dirpath=output_directory, filename=f'{paper_id}.tar.gz')

        print(f"Downloaded {i + 1}/{max_papers_per_category} papers in {category} category.")

if __name__ == "__main__":
    # Specify the subcategories under the math category
    math_subcategories = ['AG', 'AT', 'AP', 'CT', 'CA', 'CO', 'AC', 'CV', 'DS', 'FA', 'GM', 'GN', 'GT', 'GR', 'HO', 'IT',
                          'KT', 'LO', 'MP', 'MG', 'NT', 'NA', 'OA', 'OC', 'PR', 'QA', 'RT', 'RA', 'SP', 'ST']

    # Download LaTeX sources for each subcategory
    for subcategory in math_subcategories:
        download_latex_sources(subcategory)
