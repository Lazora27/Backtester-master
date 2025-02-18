import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PhaseDivergence': 1.0
        })
    )
