import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und MovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'MovingAverage': 1.0
        })
    )
