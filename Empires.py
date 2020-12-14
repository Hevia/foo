class Empire:
    def init(self, comm, comm_speed, comm_amount, fear, econ, safe, propa):
        self.comm = comm
        self.comm_speed = comm_speed
        self.comm_amount = comm_amount
        self.comm_eff = (self.comm_speed / self.comm_amount)
        self.fear = fear


# Communication
# Roads, Vehicles, Animals, Magic
# What matters is speed and amount that can be delievered
# Ineffective communication leads to problems
# Does magic impact communication?
# Slower communication can result in decentralised power which could fracture the empire

# Control
# Fear, Economic Opp, Security/Safety
# Propagonda effectiveness (becomes less effective depending on the freedom of research)
# self-governance and sovernity can change how likely the people will rebel
# Communication effectiveness will impact the stability of the empire and how effective is control
# How swiftly can an empire respond to threats?
# How well do absorbed people adjust and fit into the empire

# Commerce
# If the citizens feel as if they have a god job and stability it makes them happy
# Communication effectivness can improve commerce
# Is property protected? Is trade facilated?
# Taxes, public services, etc
# Is the legal system fair?
# A healthy economy indicates a healthy Empire. Wide mmarkets can improve the welfare and income of its citizens

# Culture, economy, politics, religion all change and how does that impact the empire


def gen_empire():
