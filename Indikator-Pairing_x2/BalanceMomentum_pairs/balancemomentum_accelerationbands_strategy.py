import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AccelerationBands': 1.0
        })
    )
