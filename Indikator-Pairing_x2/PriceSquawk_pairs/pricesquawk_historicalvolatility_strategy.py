import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
