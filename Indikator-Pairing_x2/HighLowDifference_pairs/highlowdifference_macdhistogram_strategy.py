import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MACDHistogram': 1.0
        })
    )
