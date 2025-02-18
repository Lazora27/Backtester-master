import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'DemandIndex': 1.0
        })
    )
