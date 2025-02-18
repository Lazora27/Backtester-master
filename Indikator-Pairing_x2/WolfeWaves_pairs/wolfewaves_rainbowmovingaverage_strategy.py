import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
