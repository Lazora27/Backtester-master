import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'DeltaProfile': 1.0
        })
    )
