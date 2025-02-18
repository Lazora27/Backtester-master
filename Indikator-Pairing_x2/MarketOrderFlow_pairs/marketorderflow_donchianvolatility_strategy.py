import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'DonchianVolatility': 1.0
        })
    )
