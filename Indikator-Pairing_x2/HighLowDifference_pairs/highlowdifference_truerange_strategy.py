import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und TrueRange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'TrueRange': 1.0
        })
    )
