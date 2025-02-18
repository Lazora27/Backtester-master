import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
