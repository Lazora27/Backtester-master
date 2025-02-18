import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'PhaseDivergence': 1.0
        })
    )
