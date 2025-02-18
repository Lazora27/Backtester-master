import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PriceDelta
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PriceDelta': 1.0
        })
    )
