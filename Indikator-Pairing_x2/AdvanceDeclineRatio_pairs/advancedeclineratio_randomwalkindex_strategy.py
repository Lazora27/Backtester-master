import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineRatio_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineRatio und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AdvanceDeclineRatio': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
