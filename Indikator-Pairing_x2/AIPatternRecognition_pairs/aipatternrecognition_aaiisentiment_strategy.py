import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AAIISentiment': 1.0
        })
    )
