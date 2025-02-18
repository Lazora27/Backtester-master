import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'GannAngles': 1.0
        })
    )
