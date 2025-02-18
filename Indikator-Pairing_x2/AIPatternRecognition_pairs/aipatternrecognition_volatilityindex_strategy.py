import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'VolatilityIndex': 1.0
        })
    )
