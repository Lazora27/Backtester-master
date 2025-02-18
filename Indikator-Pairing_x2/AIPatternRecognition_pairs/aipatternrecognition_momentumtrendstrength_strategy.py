import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
