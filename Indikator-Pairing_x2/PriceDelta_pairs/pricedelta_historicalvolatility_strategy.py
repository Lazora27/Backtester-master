import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
