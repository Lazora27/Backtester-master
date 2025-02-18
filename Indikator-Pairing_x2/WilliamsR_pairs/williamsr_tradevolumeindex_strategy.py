import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
