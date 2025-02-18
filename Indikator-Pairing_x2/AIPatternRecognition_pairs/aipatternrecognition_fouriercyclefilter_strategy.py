import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
