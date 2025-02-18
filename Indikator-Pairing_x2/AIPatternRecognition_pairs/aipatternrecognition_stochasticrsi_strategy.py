import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'StochasticRSI': 1.0
        })
    )
