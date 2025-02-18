import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
