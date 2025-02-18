import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TickVolume
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TickVolume': 1.0
        })
    )
