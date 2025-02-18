import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
