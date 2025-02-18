import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SuperMACD
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SuperMACD': 1.0
        })
    )
