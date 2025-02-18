import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
