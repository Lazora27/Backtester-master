import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PhaseDivergence': 1.0
        })
    )
