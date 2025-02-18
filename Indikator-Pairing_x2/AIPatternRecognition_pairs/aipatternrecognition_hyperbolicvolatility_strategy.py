import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
