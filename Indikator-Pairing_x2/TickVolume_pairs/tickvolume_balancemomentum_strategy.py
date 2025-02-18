import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'BalanceMomentum': 1.0
        })
    )
