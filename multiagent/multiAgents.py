# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util, sys

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        newAction = legalMoves[chosenIndex]


        return newAction

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        oldFood = currentGameState.getFood()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newGhostPos = [ghostState.getPosition() for ghostState in newGhostStates]
        oldScore = currentGameState.getScore()
        newScore = successorGameState.getScore()
        newFoodList = successorGameState.getFood().asList()



        newStateEval = 0
        for candy in newFoodList:
          if (util.manhattanDistance(candy, newPos) <= 5):
            newStateEval += 7

          if ((action == 'North') and (candy[0] == newPos[0]) and (candy[1] > newPos[1])):
             newStateEval += (85 - (candy[1]-newPos[1]))
          if ((action == 'South') and (candy[0] == newPos[0]) and (candy[1] < newPos[1])):
             newStateEval += (85 - (newPos[1]-candy[1]))
          if ((action == 'East') and (candy[0] > newPos[0]) and (candy[1] == newPos[1])):
             newStateEval += (85 - (candy[0] - newPos[0]))
          if ((action == 'West') and (candy[0] < newPos[0]) and (candy[1] == newPos[1])):
             newStateEval += (85 - (newPos[0]-candy[0]))
        if (newScore > oldScore):
          newStateEval += 350
        if (newFood < oldFood):
          newStateEval += 300

        for ghost in newGhostPos:

          if (ghost == newPos):
            newStateEval -= 500
          elif (util.manhattanDistance(ghost, newPos) <= 6):
            newStateEval -= 10
          elif (util.manhattanDistance(ghost, newPos) <= 3):
            newStateEval -= 75
          elif (util.manhattanDistance(ghost, newPos) <= 1):
            newStateEval -= 250
        "*** YOUR CODE HERE ***"
        'print newStateEval'
        return newStateEval

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        


        

        def minimaxDispatch(self, gameState, currentDepth, currentAgentIndex):
          if (currentDepth == (self.depth) or (gameState.isWin() or gameState.isLose())):
            return self.evaluationFunction(gameState)
          elif (currentAgentIndex == (gameState.getNumAgents() -1 )):
            return maxLayer(self, gameState, currentDepth, ((currentAgentIndex + 1)%gameState.getNumAgents()))
          else:
            return minLayer(self, gameState, currentDepth , ((currentAgentIndex + 1)%gameState.getNumAgents()))
        def maxLayer(self, gameState, currentDepth, currentAgentIndex):
          maxV = -sys.maxint - 1
          possibleActions = gameState.getLegalActions(currentAgentIndex)
          for possibleAction in possibleActions:
            possibleSuccessor = gameState.generateSuccessor(currentAgentIndex, possibleAction)
            maxV = max(maxV, minimaxDispatch(self, possibleSuccessor, currentDepth, currentAgentIndex))
          return maxV
          
        def minLayer(self, gameState, currentDepth, currentAgentIndex):
          minV = sys.maxint
          possibleActionsMin = gameState.getLegalActions(currentAgentIndex)
          if (currentAgentIndex == (gameState.getNumAgents()-1)):
            newDepth = currentDepth+1
          else:
            newDepth = currentDepth
          for possibleAction in possibleActionsMin:
            possibleSuccessor = gameState.generateSuccessor(currentAgentIndex, possibleAction)
            
            minV = min(minV, minimaxDispatch(self, possibleSuccessor, newDepth, currentAgentIndex))
          return minV


        legalMoves = gameState.getLegalActions(0)
        
        scores = []
        bestScore = -sys.maxint -1
        for move in legalMoves:
          score = minimaxDispatch(self, gameState.generateSuccessor(0, move),0,0)
          if (score >= bestScore):
            bestScore = score
            bestMove = move
      


        return bestMove

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        def alphaBetaDispatch(self, gameState, currentDepth, currentAgentIndex, alpha, beta):
          if (currentDepth == (self.depth) or (gameState.isWin() or gameState.isLose())):
            return self.evaluationFunction(gameState)
          elif (currentAgentIndex == (gameState.getNumAgents() -1 )):
            return maxLayer(self, gameState, currentDepth, ((currentAgentIndex + 1)%gameState.getNumAgents()))
          else:
            return minLayer(self, gameState, currentDepth , ((currentAgentIndex + 1)%gameState.getNumAgents()))
        def maxLayer(self, gameState, currentDepth, currentAgentIndex):
          maxV = -sys.maxint - 1
          possibleActions = gameState.getLegalActions(currentAgentIndex)
          for possibleAction in possibleActions:
            possibleSuccessor = gameState.generateSuccessor(currentAgentIndex, possibleAction)
            maxV = max(maxV, alphaBetaDispatch(self, possibleSuccessor, currentDepth, currentAgentIndex))
          return maxV
          
        def minLayer(self, gameState, currentDepth, currentAgentIndex):
          minV = sys.maxint
          possibleActionsMin = gameState.getLegalActions(currentAgentIndex)
          if (currentAgentIndex == (gameState.getNumAgents()-1)):
            newDepth = currentDepth+1
          else:
            newDepth = currentDepth
          for possibleAction in possibleActionsMin:
            possibleSuccessor = gameState.generateSuccessor(currentAgentIndex, possibleAction)
            
            minV = min(minV, alphaBetaDispatch(self, possibleSuccessor, newDepth, currentAgentIndex))
          return minV


        legalMoves = gameState.getLegalActions(0)
        
        scores = []
        bestScore = -sys.maxint -1
        for move in legalMoves:
          score = alphaBetaDispatch(self, gameState.generateSuccessor(0, move),0,0)
          if (score >= bestScore):
            bestScore = score
            bestMove = move
      


        return bestMove

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

