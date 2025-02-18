import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PhaseDivergence': 1.0
        })
    )
