import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
