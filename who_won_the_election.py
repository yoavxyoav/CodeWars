from __future__ import division

def getWinner(listOfBallots):
  candidates = set(listOfBallots)
  voters = len(listOfBallots)
  for candidate in candidates:
      votes = listOfBallots.count(candidate)
      print (candidate, votes, voters, votes/voters)
      if votes / voters > 0.5:
          return candidate
  return None
