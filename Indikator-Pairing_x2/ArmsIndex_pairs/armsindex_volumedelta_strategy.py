import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
