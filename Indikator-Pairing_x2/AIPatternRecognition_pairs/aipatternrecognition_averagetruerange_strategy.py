import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AverageTrueRange': 1.0
        })
    )
