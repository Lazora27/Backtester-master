import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
