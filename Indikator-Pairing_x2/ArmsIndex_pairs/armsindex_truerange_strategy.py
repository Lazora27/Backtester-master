import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TrueRange
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TrueRange': 1.0
        })
    )
