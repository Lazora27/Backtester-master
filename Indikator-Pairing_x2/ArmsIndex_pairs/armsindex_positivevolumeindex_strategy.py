import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
