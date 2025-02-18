import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
