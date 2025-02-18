import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
