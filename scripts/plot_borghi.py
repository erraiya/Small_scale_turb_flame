import numpy as np
import matplotlib.pyplot as plt

def _borghi_skull():
    zones = dict()
    zones["Laminar flames"] = {"x":[0.1, 10], 'y':[10, 0.1], "pos":[0.6, 0.5]}
    zones["Wrinkled flamelets"] = {"x":[1, 1e3], 'y':[1, 1], "pos":[2e2, 0.5]}
    zones["Corrugated flamelets"] = {"x":[1, 1e3], 'y':[1, 10], "pos":[2e2, 2]}
    zones["Thin reaction zones"] = {"x":[0.1, 1e3], 'y':[10, 2e2], "pos":[1e2, 40], "rot":15}
    zones["Well stirred reactor"] = {"x":[1, 92], 'y':[1, 92],
                                     "pos":[8, 35], "rot":40}

    add_text = dict()
    add_text["Broken reaction zones"] = {"pos":[15, 2e2], "rot":15.}
    add_text["$Re_t=1$"] = {"pos":[0.3, 7], "rot":-40.}
    add_text["$Ka=1$"] = {"pos":[3e2, 12], "rot":15.}
    add_text[r"$Ka_{\delta}=1$"] = {"pos":[3e2, 2.5e2], "rot":15.}
    add_text[r"$Da=1$"] = {"pos":[6, 6], "rot":40.}
    return zones, add_text

from matplotlib import (pyplot as plt,
                        rc)
from matplotlib.patches import Polygon

def _plot_borghi(cases):
    props = {"fs_ax_lbl" : 20,
             "fs_zone_lbl": 20,
             "len_ticks_maj": 8,
             "len_ticks_min": 5,
             "fs_ticks":18,
             'alpha_zones': 0.7}
    rc('font', **{'family':'serif'})
    rc('text', usetex=True)
    rc({"pgf.texsystem": "pdflatex",
        "pgf.preamble": [r"\usepackage[utf8x]{inputenc}",
                         r"\usepackage[T1]{fontenc}"]})
    zones, add_text = _borghi_skull()
    fig = plt.figure(figsize=(7, 6))
    axe = fig.add_subplot(111)
    
    pts = np.array([[0.1,0.1], [10,0.1], [0.1,10]])
    p = Polygon(pts, closed=False, color="gainsboro")
    axe.add_patch(p)

    fig.subplots_adjust(left=0.15, top=0.95, right=0.95)
    axe.set_xlabel(r'$\Lambda=l_t/\delta_L$', fontsize=props["fs_ax_lbl"])
    axe.set_ylabel(r'$\Upsilon=u^{\prime}/S_L$', fontsize=props["fs_ax_lbl"])
    for zone in zones:
        axe.loglog(zones[zone]["x"], zones[zone]["y"], lw=2, color="gray")
        rotation = 0
        if "rot" in zones[zone]:
            rotation = zones[zone]["rot"]
        axe.text(*zones[zone]["pos"], zone,
                 fontsize=15,
                 rotation=rotation,
                 horizontalalignment='center',
                 verticalalignment='top',
                 multialignment='center',
                 color="#505050")

    for zone in add_text:
        color = "r"
        alpha = props['alpha_zones']
        if "=" not in zone:
            color = "#505050"
            alpha = 0.9
        axe.text(*add_text[zone]["pos"], zone,
                 fontsize=15,
                 rotation=add_text[zone]["rot"],
                 horizontalalignment='center',
                 verticalalignment='top',
                 multialignment='center',
                 color=color,
                 alpha=alpha)

    axe.set_xlim([0.1, 1e3])
    axe.set_ylim([0.1, 1e3])
    axe.tick_params(axis="both", which="both", direction="in", top=True, right=True)
    axe.tick_params(axis="both", which="major", length=props["len_ticks_maj"])
    axe.tick_params(axis="both", which="minor", length=props["len_ticks_min"])
    for tick in axe.xaxis.get_major_ticks():
        tick.label.set_fontsize(props["fs_ticks"])
    for tick in axe.yaxis.get_major_ticks():
        tick.label.set_fontsize(props["fs_ticks"])



    colors = {r"$\mathcal{C}_1$":"k",
             r"$\mathcal{C}_2$":"b",
             r"$\mathcal{C}_3$":"r",
             r"$\mathcal{C}_4$":"purple"}

    for case in cases:
        x_val = cases[case]["x"]
        y_val = cases[case]["y"]
        color = colors[case]
        axe.plot(x_val, y_val, marker="s", color=color, markersize=10)
        axe.annotate(case, xy=(x_val*0.45, y_val*0.8), fontsize=16)
    plt.savefig("../figs/borghi.pdf")


def main():
    cases = {r"$\mathcal{C}_1$":{"x":1.75, "y":2.5},
             r"$\mathcal{C}_2$":{"x":1.75, "y":13},
             r"$\mathcal{C}_3$":{"x":1.75, "y":45},
             r"$\mathcal{C}_4$":{"x":1.75, "y":150}}
    _plot_borghi(cases)

if __name__ == '__main__':
    main()
