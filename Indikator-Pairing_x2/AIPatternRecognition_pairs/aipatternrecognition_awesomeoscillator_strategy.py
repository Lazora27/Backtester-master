import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
