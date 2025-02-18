import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
