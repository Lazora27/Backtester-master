import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
