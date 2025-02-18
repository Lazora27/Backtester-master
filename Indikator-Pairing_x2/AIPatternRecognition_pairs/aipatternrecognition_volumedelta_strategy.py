import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'VolumeDelta': 1.0
        })
    )
