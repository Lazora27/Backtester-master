import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
