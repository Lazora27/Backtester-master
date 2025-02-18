import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und VWAPBands
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'VWAPBands': 1.0
        })
    )
