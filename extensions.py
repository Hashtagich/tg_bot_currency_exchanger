class ConversionException(Exception):
    pass


class CriptoConvector:
    """Дока"""

    @staticmethod
    def get_price(base: str, quote: str, amount: str) -> str:
        result = base + quote + amount
        return result
