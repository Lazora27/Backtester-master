import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
