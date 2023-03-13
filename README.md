## Test Plan:

---

## The following test cases are made for example:
* Make sure the page loads successfully
* Check if the temperature conversion function is working properly
* Make sure that the temperature input field does not accept text values
* Make sure the temperature input field is present on the page
* Make sure the temperature input field only accepts numeric values
* Make sure that the temperature input field can take negative values.
* Make sure the temperature input field has a default value of blank.
* Make sure the page has a drop-down list of "from" units.
* Make sure the page has a drop-down list of units of measure "before"
* Verify that pressing the "convert" button returns the converted temperature value.
* Verify that when converting a negative temperature value, the correct converted value is displayed.

---

## My suggestions for test cases and their division into positive and negative tests:

## Positive testing:

* Verify that the conversion of a negative temperature value shows the correct converted value.
* Verify that the converted temperature value is displayed in the correct units.
* Verify that selecting the unit of measure "to" updates the available parameters in the "from" drop-down list.
* Make sure that selecting the unit of measure "from" updates the available parameters in the "to" drop-down list.
* Verify that the page loads successfully.
* Verify that the temperature entry field is present on the page.
* Verify that the temperature entry field can accept negative values.
* Verify that the "Clear" button resets the input fields to their default values.
* Verify that the temperature entry field has a default value of 0.
* Make sure that the "convert" button is disabled until the temperature value and both unit drop-down lists are selected.
* Make sure that the converted temperature value is accurate based on the unit of measure selected and the conversion formula.
* Verify that the page displays a message indicating that the conversion was successful.
* Verify that the page displays an error message if an invalid temperature value is entered, such as a nonnumeric value or a value that is outside the valid range.
* Make sure that an error message is displayed on the page if the selected unit is not supported.

## Negative Test:

* Verify that the temperature entry field accepts only numeric values.
* Verify that entering a decimal value in the temperature entry field results in an error message if decimal values are not supported.
* Verify that entering a value greater than the maximum supported temperature will result in an error message.
* Verify that entering a value less than the minimum supported temperature results in an error message.
* Verify that entering a value in the wrong format, such as using a comma instead of a period, results in an error message.
* Verify that selecting an unsupported unit of measure results in an error message.
* Make sure that selecting the same unit of measure "from" and "to" results in an error message.

## Some suggestions

---

#### Verify that the temperature conversion is accurate
* a. Enter a temperature value in Celsius and convert it to Fahrenheit
* b. Verify that the calculated Fahrenheit temperature is accurate
* c. Enter a temperature value in Fahrenheit and convert it to Celsius
* d. Verify that the calculated Celsius temperature is accurate
* e. Repeat steps a-d with different temperature values

#### Verify that the conversion input and output fields are functional
* a. Enter a temperature value in the Celsius input field and verify that the input is accepted
* b. Select Fahrenheit as the conversion unit and verify that the selection is accepted
* c. Click the "Convert" button and verify that the conversion is accurate and displayed in the output field
* d. Repeat steps a-c with different temperature values and unit selections

#### Verify that invalid input is handled correctly
* a. Enter a non-numeric value in the temperature input field and verify that an error message is displayed
* b. Enter a value outside the range of the selected temperature unit and verify that an error message is displayed
* c. Repeat steps a-b with different non-numeric and out-of-range values