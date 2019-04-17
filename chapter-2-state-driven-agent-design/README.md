# State-Driven Agent Design

Designing an agent can get very tricky as the behaviour of the agent
grows more complex. It can be very tempting to implement a set of rules
by using if -> then -> else rules but this can make the agent's behaviour
less flexible, hard to manage and update as well as debug.

Instead we can use a state driven design where the agent can
be in a different state at any given moment. A state
allows us to encapsulate the behaviour of the agent in easy
and concise manner.

It also allows us to debug the agent very quickly when there is
a bug in our logic as the only thing we need to do is finding
which state of the agent is the offending one. Then we can
either use breakpoints to go through the logic of the state
or simply add some print statements.

Each state has a set of inherited method named: enter, execute, exit
and on_message. Based on our needs we can introduce more methods
that would allow for more complex behaviour.

a). Enter method

The enter method allows us to run some logic as the agent is about
to enter the state. This can be either cleaning up, or setting up
required parameters.

b). Execute method

The execute method will contain the main logic that describes the
behaviour of the state.

c). Exit method

The exit method gives us a last point before we leave the state
to enter another state to run any piece of logic.

d). On message method

Last but not least the on message method allows a state to receive
asynchronous messages. This way states can be given messages from the outside
world in order to invoke some logic or event to be informed to
to change to another state.

An example would be as an agent is patrolling an area and he is
in a patrol state he can be notified that there is an issue in a different
area and he can change to state to seek that area in order to find an
intruder.