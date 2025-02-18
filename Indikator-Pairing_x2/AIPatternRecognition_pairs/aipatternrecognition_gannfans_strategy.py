import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und GannFans
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'GannFans': 1.0
        })
    )
