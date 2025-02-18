import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
