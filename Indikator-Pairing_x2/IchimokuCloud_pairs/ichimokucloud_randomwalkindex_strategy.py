import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
