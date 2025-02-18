import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
