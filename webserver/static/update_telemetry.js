function get_telemetry_data()
{
    return "Elevation: 125, Azimuth: 0";
};

window.onload = function() {
    //using the function
    telemetry_label = document.getElementsByClassName("telemetry")[0];
    console.log(telemetry_label);
    telemetry_label.textContent = `${get_telemetry_data()}`
}
  