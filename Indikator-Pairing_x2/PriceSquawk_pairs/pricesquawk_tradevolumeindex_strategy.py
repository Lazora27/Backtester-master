import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
