import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WolfeWaves': 1.0
        })
    )
