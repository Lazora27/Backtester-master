import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'FlowOfFunds': 1.0
        })
    )
