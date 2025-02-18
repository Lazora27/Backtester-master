import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CycleFinder': 1.0
        })
    )
