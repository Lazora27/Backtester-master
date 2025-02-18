import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
