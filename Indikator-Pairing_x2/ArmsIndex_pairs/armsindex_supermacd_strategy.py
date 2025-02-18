import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
