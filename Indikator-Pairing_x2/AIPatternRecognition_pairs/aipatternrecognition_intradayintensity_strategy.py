import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'IntradayIntensity': 1.0
        })
    )
