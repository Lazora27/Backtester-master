import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CenterOfGravity': 1.0
        })
    )
