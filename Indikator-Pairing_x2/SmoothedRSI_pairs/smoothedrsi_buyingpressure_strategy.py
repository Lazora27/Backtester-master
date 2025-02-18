import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
