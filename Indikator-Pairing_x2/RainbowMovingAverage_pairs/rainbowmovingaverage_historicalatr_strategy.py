import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'HistoricalATR': 1.0
        })
    )
