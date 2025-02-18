import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und CyberCycle
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'CyberCycle': 1.0
        })
    )
