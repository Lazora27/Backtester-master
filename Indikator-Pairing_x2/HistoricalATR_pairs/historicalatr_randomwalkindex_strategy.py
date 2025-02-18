import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
