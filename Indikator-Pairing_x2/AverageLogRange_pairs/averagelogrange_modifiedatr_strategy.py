import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'ModifiedATR': 1.0
        })
    )
