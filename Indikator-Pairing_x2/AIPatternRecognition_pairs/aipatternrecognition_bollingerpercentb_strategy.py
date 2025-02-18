import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BollingerPercentB': 1.0
        })
    )
