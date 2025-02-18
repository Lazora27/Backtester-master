import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'IchimokuCloud': 1.0
        })
    )
