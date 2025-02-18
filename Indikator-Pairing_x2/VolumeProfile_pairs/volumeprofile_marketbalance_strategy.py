import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MarketBalance': 1.0
        })
    )
