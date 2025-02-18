import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
