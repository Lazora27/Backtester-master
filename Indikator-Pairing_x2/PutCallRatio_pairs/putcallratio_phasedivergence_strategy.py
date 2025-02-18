import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PhaseDivergence': 1.0
        })
    )
