import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
