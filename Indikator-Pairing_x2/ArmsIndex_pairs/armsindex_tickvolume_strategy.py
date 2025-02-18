import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TickVolume
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TickVolume': 1.0
        })
    )
