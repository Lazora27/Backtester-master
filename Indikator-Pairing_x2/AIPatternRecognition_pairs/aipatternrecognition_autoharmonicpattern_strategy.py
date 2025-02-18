import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
