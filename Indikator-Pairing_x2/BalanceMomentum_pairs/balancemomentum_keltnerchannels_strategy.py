import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'KeltnerChannels': 1.0
        })
    )
