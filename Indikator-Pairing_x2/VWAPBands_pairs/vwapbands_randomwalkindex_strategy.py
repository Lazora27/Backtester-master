import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
