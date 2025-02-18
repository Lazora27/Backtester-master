import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
