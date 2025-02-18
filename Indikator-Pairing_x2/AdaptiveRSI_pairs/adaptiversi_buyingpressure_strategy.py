import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
