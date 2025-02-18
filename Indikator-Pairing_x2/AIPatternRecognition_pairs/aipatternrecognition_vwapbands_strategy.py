import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'VWAPBands': 1.0
        })
    )
