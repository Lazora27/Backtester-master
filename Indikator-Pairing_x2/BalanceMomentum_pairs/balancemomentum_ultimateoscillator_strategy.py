import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'UltimateOscillator': 1.0
        })
    )
