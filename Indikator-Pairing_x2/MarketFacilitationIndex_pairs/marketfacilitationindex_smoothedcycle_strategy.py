import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
