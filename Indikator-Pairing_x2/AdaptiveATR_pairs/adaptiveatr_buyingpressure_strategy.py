import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'BuyingPressure': 1.0
        })
    )
