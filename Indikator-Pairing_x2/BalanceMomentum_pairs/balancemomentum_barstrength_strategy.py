import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BarStrength
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BarStrength': 1.0
        })
    )
