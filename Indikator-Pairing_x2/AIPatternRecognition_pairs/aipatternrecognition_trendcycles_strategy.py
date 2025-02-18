import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'TrendCycles': 1.0
        })
    )
