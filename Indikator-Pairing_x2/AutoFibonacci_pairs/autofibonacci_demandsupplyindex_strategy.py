import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
