import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BuyingPressure': 1.0
        })
    )
