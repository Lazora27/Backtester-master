import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
