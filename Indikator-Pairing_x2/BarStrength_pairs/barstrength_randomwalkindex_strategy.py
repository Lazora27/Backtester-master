import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
