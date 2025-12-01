# LangChain Compensation Example

This directory contains a comprehensive example demonstrating `langchain-compensation` v0.4.0 with Google Gemini.

## Example

**ecommerce_order.py** - Complete e-commerce order processing system demonstrating:

- Automatic compensation on failure
- CompensationSchema for declarative parameter mapping
- Multi-step workflow with dependency-aware rollback
- Error detection and handling

## Structure

- `tools.py` - All tool definitions (inventory, orders, payments, shipping)
- `ecommerce_order.py` - Main example demonstrating the workflow

## Running the Example

```bash
# Install dependencies
pip install langchain-compensation langchain-google-genai python-dotenv

# Set up API key in .env file
echo "GOOGLE_API_KEY=your-key-here" > .env

# Run the example
python ecommerce_order.py
```

## Requirements

- Python 3.9+
- langchain-compensation >= 0.4.0
- langchain >= 1.0.0
- langchain-google-genai
- python-dotenv

## Workflow

The example demonstrates an e-commerce order processing workflow:

1. Reserve inventory for products
2. Create the order
3. Process payment
4. Create shipment

If any step fails (e.g., payment exceeds limit), all previous steps are automatically compensated in reverse order.
