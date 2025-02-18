import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'Fisher': 1.0
        })
    )
