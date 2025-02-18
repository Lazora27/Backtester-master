import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
