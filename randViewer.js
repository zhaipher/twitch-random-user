var channelName = "zhaipher"; // ใส่ชื่อช่อง Twitch ของคุณที่นี่
var twitchAPIUrl = `https://tmi.twitch.tv/group/user/${channelName}/chatters`;

fetch(twitchAPIUrl)
  .then(response => response.json())
  .then(data => {
    var viewers = data.chatters.viewers;
    var moderators = data.chatters.moderators;
    var broadcaster = data.chatters.broadcaster;
    var allViewers = viewers.concat(moderators, broadcaster);
    var randomViewer = allViewers[Math.floor(Math.random() * allViewers.length)];
    if (randomViewer) {
      randomViewer;
    } else {
      "ไม่มีผู้ชมในปัจจุบัน";
    }
  })
  .catch(error => {
    "เกิดข้อผิดพลาดในการดึงข้อมูลผู้ชม";
  });
