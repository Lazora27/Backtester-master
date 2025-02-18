import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
