import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
