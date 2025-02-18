import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BollingerBands': 1.0
        })
    )
