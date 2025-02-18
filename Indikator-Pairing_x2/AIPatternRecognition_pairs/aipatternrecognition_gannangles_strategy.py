import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und GannAngles
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'GannAngles': 1.0
        })
    )
