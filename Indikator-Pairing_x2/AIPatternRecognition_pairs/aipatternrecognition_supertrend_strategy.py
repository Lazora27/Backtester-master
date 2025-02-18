import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SuperTrend': 1.0
        })
    )
