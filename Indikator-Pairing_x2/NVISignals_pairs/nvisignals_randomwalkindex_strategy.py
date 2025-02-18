import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
