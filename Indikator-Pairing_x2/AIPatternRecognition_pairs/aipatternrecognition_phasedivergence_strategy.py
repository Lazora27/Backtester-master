import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'PhaseDivergence': 1.0
        })
    )
