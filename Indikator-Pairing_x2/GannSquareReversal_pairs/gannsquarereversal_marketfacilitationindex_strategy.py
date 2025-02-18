import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
