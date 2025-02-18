import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
