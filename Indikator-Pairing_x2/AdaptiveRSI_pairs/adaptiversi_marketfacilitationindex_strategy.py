import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
