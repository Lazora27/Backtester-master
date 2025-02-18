import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MarketBalance': 1.0
        })
    )
