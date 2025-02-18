import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
