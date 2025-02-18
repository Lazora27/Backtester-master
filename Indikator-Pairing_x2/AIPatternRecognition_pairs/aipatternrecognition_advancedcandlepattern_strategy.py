import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
