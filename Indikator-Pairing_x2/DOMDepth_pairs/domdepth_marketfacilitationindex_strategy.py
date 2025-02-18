import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
