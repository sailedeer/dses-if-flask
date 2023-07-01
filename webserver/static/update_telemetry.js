function get_telemetry_data()
{
    // Issue #4: use real-time mqtt data
    return "Elevation: 125, Azimuth: 0";
};

window.onload = function() {
    telemetry_label = document.getElementsByClassName("telemetry")[0];
    telemetry_label.textContent = `${get_telemetry_data()}`
}
