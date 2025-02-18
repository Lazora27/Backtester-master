import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
