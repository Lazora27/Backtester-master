import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
