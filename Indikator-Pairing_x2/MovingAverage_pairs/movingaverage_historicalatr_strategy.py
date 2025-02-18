import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'HistoricalATR': 1.0
        })
    )
