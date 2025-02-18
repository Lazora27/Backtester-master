import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'AccelerationBands': 1.0
        })
    )
