import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
