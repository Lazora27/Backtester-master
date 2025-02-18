import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
