import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
