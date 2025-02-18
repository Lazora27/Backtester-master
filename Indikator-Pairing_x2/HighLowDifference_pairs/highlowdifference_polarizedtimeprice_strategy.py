import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
