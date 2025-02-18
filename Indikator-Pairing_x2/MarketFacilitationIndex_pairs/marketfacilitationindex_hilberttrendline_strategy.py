import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
