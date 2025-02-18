import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'BuyingPressure': 1.0
        })
    )
