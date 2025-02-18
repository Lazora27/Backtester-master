import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AutoSupportResistance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AutoSupportResistance
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AutoSupportResistance': 1.0
        })
    )
