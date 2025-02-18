import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'CoppockCurve': 1.0
        })
    )
