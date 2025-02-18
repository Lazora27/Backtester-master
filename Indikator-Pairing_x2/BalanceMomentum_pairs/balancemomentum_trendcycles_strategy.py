import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TrendCycles': 1.0
        })
    )
