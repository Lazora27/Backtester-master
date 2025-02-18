import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CumulativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CumulativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CumulativeVolumeIndex': 1.0
        })
    )
