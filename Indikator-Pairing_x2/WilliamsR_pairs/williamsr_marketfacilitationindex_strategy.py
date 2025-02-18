import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
