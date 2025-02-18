import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'HistoricalATR': 1.0
        })
    )
