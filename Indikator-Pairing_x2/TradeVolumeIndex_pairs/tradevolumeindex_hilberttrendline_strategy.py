import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
