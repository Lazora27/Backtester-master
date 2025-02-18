import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PriceSquawk': 1.0
        })
    )
