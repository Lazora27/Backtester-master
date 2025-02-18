import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TRIXIndicator': 1.0
        })
    )
