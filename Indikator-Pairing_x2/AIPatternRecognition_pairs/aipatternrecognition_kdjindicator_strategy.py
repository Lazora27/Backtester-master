import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'KDJIndicator': 1.0
        })
    )
