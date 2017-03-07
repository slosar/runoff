#
# runoff election voting
#

from __future__ import print_function, division

def runoff(cnames, votes):
    """ Determines winner of a runoff election using ranked list instant runoff scheme.
    Input:
    
    cnames -- list of candidate names. This also determines number of candidates

    votes -- list of votes. Each vote is another list that maps candidate names in rank order
             for that particular vote, starting from 1. Zero means this candidate is not ranked and vote
             won't be counted once the preferences have been exhausted.

    Output:

    None  -- Look at the printout, that contains information.
   """

    Nc=len(cnames)
    print ("We have %i candidates:"%Nc)
    for n in cnames:
        print ("   %s"%n)

    print ("Checking vote sanity, converting to ranked list...")

    ## we will convert votes to a list of preferences, indexing candidates
    pvotes=[]
    for vote in votes:
        try:
            assert(len(vote)==Nc)
            ## get rid of zeros and ensure the rest are ascending from 1
            slist=sorted(filter(bool,vote))
            assert(slist==range(1,len(slist)+1))
        except AssertionError:
            print ("Something wrong with the vote: ",vote)
            continue
        except:
            print ("Coding error of some kind\n")
            stop()
        pvotes.append([vote.index(x) for x in slist])

    ## list of candidates still in play
    inplay=range(Nc)
    for ir in range(Nc):
        print ("---------------------")
        print ("Round %i"%ir)
        nvotes={}
        for i in inplay:
            nvotes[i]=0
        tvotes=0
        for pv in pvotes:
            for p in pv:
                if p in inplay:
                    nvotes[p]+=1
                    tvotes+=1
                    break
        ## now print results
        for i in inplay:
            print("Candidate %i (%s) : %i (%3.1f percent)"%(i,cnames[i],nvotes[i],nvotes[i]*100/tvotes))
        towin=tvotes/2
        print ("To win need %i votes."%towin)
        have_winner=False
        for i in inplay:
            if nvotes[i]>towin: ## Yes, this is absolute bigger, not >=
                print ("** We have a winner: %s **"%cnames[i])
                have_winner=True
                break
        if have_winner:
            break
        ## Remove the worst candidate(s)
        ## in principle, there could be multiple with equal, lowerst number of votes.
        worstn=min(nvotes.values())
        for i in nvotes.keys():
            if nvotes[i]==worstn:
                print("Removing candidate %i (%s)"%(i,cnames[i]))
                inplay.pop(i)

    print("Done.")
    return None
    
    
                
                
