import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
