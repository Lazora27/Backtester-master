import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'UlcerIndex': 1.0
        })
    )
