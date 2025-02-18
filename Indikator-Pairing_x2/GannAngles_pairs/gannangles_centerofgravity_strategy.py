import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CenterOfGravity': 1.0
        })
    )
