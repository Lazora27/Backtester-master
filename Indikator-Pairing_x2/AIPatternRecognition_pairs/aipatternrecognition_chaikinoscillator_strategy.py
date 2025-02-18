import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
