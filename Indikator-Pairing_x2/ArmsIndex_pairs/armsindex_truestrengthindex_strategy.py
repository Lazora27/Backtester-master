import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
