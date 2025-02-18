import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ModifiedATR': 1.0
        })
    )
