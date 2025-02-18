import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DonchianChannels': 1.0
        })
    )
