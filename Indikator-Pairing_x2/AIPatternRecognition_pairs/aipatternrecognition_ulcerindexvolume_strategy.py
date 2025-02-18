import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
