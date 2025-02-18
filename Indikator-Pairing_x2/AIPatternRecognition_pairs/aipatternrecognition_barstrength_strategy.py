import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und BarStrength
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'BarStrength': 1.0
        })
    )
