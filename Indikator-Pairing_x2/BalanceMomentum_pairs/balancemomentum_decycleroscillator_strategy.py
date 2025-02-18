import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
