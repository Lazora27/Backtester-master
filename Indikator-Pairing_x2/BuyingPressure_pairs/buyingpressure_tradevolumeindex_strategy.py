import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
