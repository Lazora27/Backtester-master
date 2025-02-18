import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HilbertSinewave': 1.0
        })
    )
