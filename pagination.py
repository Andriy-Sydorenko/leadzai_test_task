def generate_pagination(current_page, total_pages, boundaries, around):
    if current_page < 1 or current_page > total_pages or total_pages < 1 or boundaries < 0 or around < 0:
        return "Invalid input"
    pages = []

    # Determine the first and last page numbers to be displayed based on boundaries
    start_pages = list(range(1, min(boundaries, total_pages) + 1))
    end_pages = list(range(max(total_pages - boundaries + 1, boundaries + 1), total_pages + 1))

    # Determine the pages around the current page
    around_pages = list(range(max(current_page - around, min(boundaries + 1, total_pages)),
                              min(current_page + around + 1, total_pages + 1)))

    # Combine the page ranges, ensuring no duplicates and in order
    all_pages = sorted(set(start_pages + around_pages + end_pages))

    # Construct the pagination string with ellipses where there are gaps in the page sequence
    for i in range(len(all_pages)):
        # Add the current page number
        pages.append(str(all_pages[i]))

        # Check if we need to add ellipses
        if i < len(all_pages) - 1:
            if all_pages[i + 1] - all_pages[i] > 1:
                pages.append("...")

    return ' '.join(pages)
