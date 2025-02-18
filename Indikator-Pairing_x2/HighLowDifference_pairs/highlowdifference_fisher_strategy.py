import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und Fisher
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'Fisher': 1.0
        })
    )
