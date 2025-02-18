import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
