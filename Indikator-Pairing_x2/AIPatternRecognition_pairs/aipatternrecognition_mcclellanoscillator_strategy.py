import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'McClellanOscillator': 1.0
        })
    )
