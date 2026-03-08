# 📚 Book Parser

A comprehensive web scraping project that extracts book information from books.toscrape.com using multiple techniques including BeautifulSoup, Selenium, and Streamlit.

## 🎯 Features

- **Multi-level scraping approaches** (Basic → Advanced → Automation)
- **BeautifulSoup scraping** for static content extraction
- **Selenium automation** for dynamic content and user interactions
- **Streamlit web interface** for user-friendly automation
- **LinkedIn automation** capabilities
- **Add to basket functionality** testing
- **Data export** to JSON format

## 📁 Project Structure

```
Book_Parser/
├── p1.py              # Basic BeautifulSoup scraper
├── level1.py          # Level 1 scraping
├── level2.py          # Advanced Selenium scraping with pagination
├── level3.py          # LinkedIn automation
├── requirements.txt   # Python dependencies
├── books_selenium.json # Scraped data output
└── README.md          # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Chrome browser
- ChromeDriver (automatically managed by webdriver_manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SAMITH-07/book-parser.git
   cd book-parser
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

- `selenium` - Web browser automation
- `requests` - HTTP requests
- `bs4` (BeautifulSoup) - HTML parsing
- `webdriver_manager` - Automatic ChromeDriver management
- `streamlit` - Web interface framework

## 📖 Usage

### 1. Basic Web Scraping (BeautifulSoup)

```bash
python p1.py
```

**Features:**
- Scrapes book titles, prices, ratings, and availability
- Extracts image URLs and pagination info
- Outputs data to console

### 2. Advanced Selenium Scraping

```bash
python level2.py
```

**Features:**
- Multi-page scraping with pagination
- JSON data export
- Configurable page limits
- Error handling and retries

### 3. LinkedIn Automation

```bash
python level3.py
```

**Features:**
- Automated LinkedIn login
- Chrome driver management
- Session handling

### 4. Streamlit Web Interface

```bash
streamlit run streamlit_app.py
```

**Features:**
- User-friendly web interface
- Secure credential input
- Real-time automation control
- Configuration options

### 5. Add to Basket Testing

```bash
python add_to_basket.py
```

**Features:**
- Tests add to basket functionality
- Verifies basket behavior
- Demonstrates e-commerce scraping

### 6. Scrape After Add to Basket

```bash
python scrape_after_add_basket.py
```

**Features:**
- Clicks add to basket button
- Scrapes detailed book information
- Comprehensive data extraction

## 🔧 Configuration

### Chrome Driver Setup

The project uses `webdriver_manager` to automatically manage ChromeDriver, so no manual setup is required.

### Customization

- **Page limits**: Modify `pages` variable in `level2.py`
- **Output format**: Change JSON export settings
- **Wait times**: Adjust Selenium wait conditions
- **Credentials**: Update in Streamlit interface or environment variables

## 📊 Data Output

### Scraped Book Information

- **Title**: Book name
- **Price**: Cost in GBP
- **Rating**: Star rating (1-5)
- **Availability**: Stock status
- **Image URL**: Cover image link
- **Category**: Book category
- **UPC**: Product code
- **Description**: Book description
- **Reviews**: Number of reviews

### JSON Structure

```json
{
    "title": "Book Title",
    "price": "£51.77",
    "rating": "Three",
    "image_url": "https://books.toscrape.com/media/cache/...",
    "availability": "In stock",
    "category": "Fiction",
    "upc": "1234567890",
    "description": "Book description here...",
    "reviews": "0"
}
```

## 🌐 Target Website

**books.toscrape.com** - A dedicated website for web scraping practice featuring:
- 1000+ books across 50 pages
- Multiple categories
- Detailed product pages
- Pagination system
- Add to basket functionality (simulated)

## ⚠️ Important Notes

### Educational Purpose
This project is designed for **educational purposes only** to learn web scraping techniques.

### LinkedIn Automation
- Use responsibly and in accordance with LinkedIn's Terms of Service
- Never share credentials
- Consider rate limiting and respectful automation

### Legal Considerations
- Always check `robots.txt` files
- Respect website terms of service
- Implement proper rate limiting
- Don't overload servers

## 🛠️ Troubleshooting

### Common Issues

1. **ChromeDriver Issues**
   - Solution: Uses webdriver_manager for automatic management

2. **Element Not Found**
   - Solution: Check website structure changes
   - Update CSS selectors

3. **Rate Limiting**
   - Solution: Add delays between requests
   - Use proper wait conditions

4. **Login Failures**
   - Solution: Verify credentials
   - Check for CAPTCHA requirements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is for educational purposes. Please use responsibly and in accordance with website terms of service.

## 🙏 Acknowledgments

- **books.toscrape.com** - For providing a scraping practice environment
- **Selenium** - Web browser automation framework
- **BeautifulSoup** - HTML parsing library
- **Streamlit** - Web app framework

## 📞 Contact

Created by [SAMITH-07](https://github.com/SAMITH-07)

---

**Happy Scraping! 🚀**
