import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
