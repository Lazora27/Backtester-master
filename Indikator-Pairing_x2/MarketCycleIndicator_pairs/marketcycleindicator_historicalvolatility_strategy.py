import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
