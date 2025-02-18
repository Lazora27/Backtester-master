import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
