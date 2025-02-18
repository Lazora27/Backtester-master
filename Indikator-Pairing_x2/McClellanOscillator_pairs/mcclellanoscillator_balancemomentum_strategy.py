import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'BalanceMomentum': 1.0
        })
    )
