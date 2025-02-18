import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
