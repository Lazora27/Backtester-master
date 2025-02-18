import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BalanceMomentum': 1.0
        })
    )
