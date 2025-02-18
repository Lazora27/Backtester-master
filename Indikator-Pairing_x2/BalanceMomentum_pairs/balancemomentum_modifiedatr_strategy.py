import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ModifiedATR': 1.0
        })
    )
