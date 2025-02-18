import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
