import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
