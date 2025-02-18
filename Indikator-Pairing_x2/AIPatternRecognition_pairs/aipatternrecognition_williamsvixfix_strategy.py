import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
