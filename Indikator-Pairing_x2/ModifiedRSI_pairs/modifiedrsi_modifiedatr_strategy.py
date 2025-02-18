import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
