Insights:
--Potential Improvements:
1. Support for .xls files
2. UI for viewing SUM and Tables.
3. Allow row selection by index.
<br><br/>
--Missed Edge cases:
1. Merged or empty rows.
2. Values with '%' or non-numeric replaced as NaN.
3. Name mismatch due to whitespace.
4. Corrupted file.
<br><br/>
BASE URL:
http://localhost:9090
ENDPOINTS:
http://localhost:9090/list_tables

http://localhost:9090/get_table_details?table_name=CapBudgWS

http://localhost:9090/row_sum?table_name=CapBudgWS&row_name=Tax Credit (if any )="
