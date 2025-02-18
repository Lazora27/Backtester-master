import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
