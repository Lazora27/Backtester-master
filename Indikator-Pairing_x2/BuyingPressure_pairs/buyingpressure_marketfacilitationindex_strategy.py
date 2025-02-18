import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
