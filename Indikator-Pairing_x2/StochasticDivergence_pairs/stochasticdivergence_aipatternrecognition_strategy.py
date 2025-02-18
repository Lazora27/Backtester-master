import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_AIPatternRecognition_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und AIPatternRecognition
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'AIPatternRecognition': 1.0
        })
    )
