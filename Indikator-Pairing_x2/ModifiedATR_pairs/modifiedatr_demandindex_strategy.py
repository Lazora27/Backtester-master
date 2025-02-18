import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'DemandIndex': 1.0
        })
    )
