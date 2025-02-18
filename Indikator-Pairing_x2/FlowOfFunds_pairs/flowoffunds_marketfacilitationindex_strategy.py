import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
