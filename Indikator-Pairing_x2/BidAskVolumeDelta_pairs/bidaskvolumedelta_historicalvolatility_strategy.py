import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BidAskVolumeDelta_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BidAskVolumeDelta und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'BidAskVolumeDelta': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
