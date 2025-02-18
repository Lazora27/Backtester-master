import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
