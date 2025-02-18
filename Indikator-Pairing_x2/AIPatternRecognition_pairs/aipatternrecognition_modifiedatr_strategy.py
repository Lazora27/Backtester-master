import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'ModifiedATR': 1.0
        })
    )
