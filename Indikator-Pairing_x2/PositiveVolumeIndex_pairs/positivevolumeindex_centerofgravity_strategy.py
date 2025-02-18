import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
