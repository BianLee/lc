class Solution:
    def numberToWords(self, num: int) -> str:

            
        # Special case: if num is 0, return "Zero"
        if num == 0:
            return 'Zero'

        # List for numbers less than 20
        lt20 = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]

        # List for multiples of 10 (20, 30, ..., 90)
        tens = [
            '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 
            'Seventy', 'Eighty', 'Ninety'
        ]

        # List for large place values (Billion, Million, Thousand, and empty for smaller numbers)
        thousands = ['Billion', 'Million', 'Thousand', '']

        # Helper function to convert numbers less than 1000 to words
        def transfer(num):
            if num == 0:
                return ''  # If number is zero, return an empty string
            if num < 20:
                return lt20[num] + ' '  # For numbers less than 20, directly map using lt20
            if num < 100:
                return tens[num // 10] + ' ' + transfer(num % 10)  # Handle tens and remainder
            # For numbers 100 or more, handle hundreds and recursively process the remainder
            return lt20[num // 100] + ' Hundred ' + transfer(num % 100)

        # List to store the parts of the number in words
        res = []
        i, j = 1000000000, 0  # Start with billions (10^9), j is the index for `thousands`
        
        # Loop through the number in chunks of 1000
        while i > 0:
            if num // i != 0:  # If the current chunk (num // i) is non-zero
                res.append(transfer(num // i))  # Convert that chunk to words
                res.append(thousands[j])  # Append the corresponding large place value (Billion, Million, etc.)
                res.append(' ')  # Append a space for readability
            num %= i  # Remove the processed chunk from num
            j += 1  # Move to the next place value (Million, Thousand, etc.)
            i //= 1000  # Reduce i by a factor of 1000 (to move to Million, Thousand, and so on)

        # Join all parts into a single string, remove extra spaces, and return the result
        return ''.join(res).strip()
