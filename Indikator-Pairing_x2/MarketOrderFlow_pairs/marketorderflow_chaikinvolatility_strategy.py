import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
