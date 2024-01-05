// priority: 0

// Visit the wiki for more info - https://kubejs.com/

let userPoints = {}

PlayerEvents.chat(player => {

  if(player.message.trim().startsWith('~tp')){
    const playername = player.getUsername()
    const tpCommand = player.message.trim().split(' ')
    if(tpCommand.length > 2){
      player.player.tell(Text.red("Nope! You cannot tp to anywhere you want!"));
      player.cancel()
      return
    }
    if(!tpCommand[1]){
      player.player.tell(Text.red("Specify destination!"));
      player.cancel()
      return
    }
    const coords = {
      x: player.player.getX().toFixed(),
      y: player.player.getY().toFixed(),
      z: player.player.getZ().toFixed()
    }
    player.server.tell(Text.gray(`${playername}: teleported to ${tpCommand[1]}`))
    Utils.server.runCommandSilent(`/tp ${playername} ${tpCommand[1]}`)
    Utils.server.runCommandSilent(`/playsound minecraft:entity.experience_orb.pickup player @a ${coords.x} ${coords.y} ${coords.z} 1 1.6`)
    player.cancel()
  }


  if(player.message.trim().startsWith('~setpoint')){
    const coords = {
      x:player.entity.getBlockX(),
      y: player.entity.getY().toFixed(4),
      z: player.entity.getBlockZ()
    }
    userPoints[player.getUsername()] = {
      x: coords.x,
      y: coords.y,
      z: coords.z,
    }
    player.player.tell(Text.blue(`Point set at x:${coords.x} y:${coords.y} z:${coords.z}`))
    player.cancel()
  }


  if(player.message.startsWith('~point')){
    const playername = player.getUsername()
    if(!userPoints[playername]){
      player.player.tell(Text.red("You haven't set any points!"));
      player.cancel()
      return
    }
    player.player.tell(Text.gray(`Teleported to your point`))
    Utils.server.runCommandSilent(`/tp ${playername} ${userPoints[playername].x} ${userPoints[playername].y} ${userPoints[playername].z}`)
    Utils.server.runCommandSilent(`/playsound minecraft:entity.experience_orb.pickup player @a ${userPoints[playername].x} ${userPoints[playername].y} ${userPoints[playername].z} 1 1.6`)
    player.cancel()
  }


  if(player.message.startsWith('~fireball')){
    const degs = {
      x: player.entity.xRotO/10,
      y: player.entity.yRotO/10,
    }
    player.player.tell(Text.lightPurple(`x: ${degs.x} y: ${degs.y}`))
    player.cancel()
  }

  
  if(player.message.startsWith('~stop')){
    const stopCommand = player.message.trim().split(" ")
    player.server.tell(Text.gold(`${player.getUsername()} called /stop`))
    player.server.tell(Text.gold(`The server will be stoped in ${stopCommand[1] ? stopCommand[1] : "10"} seconds`))
    stopServer(stopCommand[1] ? stopCommand[1] : "10", player)
    player.cancel()
  }
})

function stopServer(time, player){
  let counter = time
  const shutdownint = setInterval(() => {
    if(counter <= 10){
      player.server.tell(Text.aqua(`Shutting down in: ${counter}`))
    }
    if(counter === 0){
      Utils.server.runCommandSilent(`/stop`)
      clearInterval(shutdownint)
    }
    counter -= 1
  }, 1000);
}