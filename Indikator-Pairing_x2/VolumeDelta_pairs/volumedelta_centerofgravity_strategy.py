import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'CenterOfGravity': 1.0
        })
    )
