import speedtest

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000
    ping_result = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping_result:.2f} ms")

test_speed()