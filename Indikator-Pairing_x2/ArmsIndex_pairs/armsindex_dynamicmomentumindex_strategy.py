import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
