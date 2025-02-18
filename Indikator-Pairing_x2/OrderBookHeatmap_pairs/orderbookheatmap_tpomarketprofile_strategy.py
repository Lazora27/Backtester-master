import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
