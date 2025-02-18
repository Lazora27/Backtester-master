import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BuyingPressure': 1.0
        })
    )
