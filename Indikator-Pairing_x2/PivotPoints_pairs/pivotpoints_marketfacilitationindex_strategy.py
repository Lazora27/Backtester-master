import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
