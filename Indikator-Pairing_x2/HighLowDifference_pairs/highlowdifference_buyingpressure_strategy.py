import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BuyingPressure': 1.0
        })
    )
