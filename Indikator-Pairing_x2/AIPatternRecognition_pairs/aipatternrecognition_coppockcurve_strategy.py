import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'CoppockCurve': 1.0
        })
    )
