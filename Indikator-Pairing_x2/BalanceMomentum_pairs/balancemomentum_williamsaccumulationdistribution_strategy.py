import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WilliamsAccumulationDistribution_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WilliamsAccumulationDistribution
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WilliamsAccumulationDistribution': 1.0
        })
    )
