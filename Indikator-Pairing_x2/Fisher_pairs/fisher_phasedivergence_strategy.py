import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PhaseDivergence': 1.0
        })
    )
