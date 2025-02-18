import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
