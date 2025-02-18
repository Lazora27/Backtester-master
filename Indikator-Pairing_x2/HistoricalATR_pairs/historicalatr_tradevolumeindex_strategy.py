import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
