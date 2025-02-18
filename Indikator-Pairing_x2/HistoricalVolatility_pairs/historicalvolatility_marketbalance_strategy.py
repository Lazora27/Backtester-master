import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und MarketBalance
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'MarketBalance': 1.0
        })
    )
