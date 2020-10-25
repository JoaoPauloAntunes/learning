# import required libraries
import uvicorn
from vidgear.gears.asyncio import WebGear

#various performance tweaks
options={"frame_size_reduction": 40, "frame_jpeg_quality": 80, "frame_jpeg_optimize": True, "frame_jpeg_progressive": False}

#initialize WebGear app  
web=WebGear(source="foo.mp4", logging=True, **options)

#run this app on Uvicorn server at address http://localhost:8000/
uvicorn.run(web(), host='localhost', port=8000)

#close app safely
web.shutdown()