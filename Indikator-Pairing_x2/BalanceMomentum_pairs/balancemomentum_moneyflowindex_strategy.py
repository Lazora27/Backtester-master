import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
