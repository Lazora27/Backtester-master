import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'HistoricalATR': 1.0
        })
    )
