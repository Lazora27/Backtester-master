import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
