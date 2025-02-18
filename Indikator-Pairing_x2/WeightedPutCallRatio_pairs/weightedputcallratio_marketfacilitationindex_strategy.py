import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
