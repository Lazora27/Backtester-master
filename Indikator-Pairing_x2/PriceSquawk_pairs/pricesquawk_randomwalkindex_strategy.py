import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
