import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ModifiedATR': 1.0
        })
    )
