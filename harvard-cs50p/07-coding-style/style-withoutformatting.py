search_result = {
 "resultCount":1,
 "results": [
{"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440868131, "trackId":1440868258, "artistName":"Weezer", "collectionName":"Weezer (Green Album)", "trackName":"Island In the Sun", "collectionCensoredName":"Weezer (Green Album)", "trackCensoredName":"Island In the Sun", "artistViewUrl":"https://music.apple.com/us/artist/weezer/115234?uo=4"
}
 ]
}
for result in search_result["results"]:
 print(result["trackName"]) # this will print the track name of the first result
