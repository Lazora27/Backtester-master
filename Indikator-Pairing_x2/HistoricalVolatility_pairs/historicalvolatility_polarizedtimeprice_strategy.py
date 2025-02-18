import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
