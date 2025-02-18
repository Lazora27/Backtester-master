import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'PhaseDivergence': 1.0
        })
    )
