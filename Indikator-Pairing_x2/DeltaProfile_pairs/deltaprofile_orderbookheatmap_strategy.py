import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
