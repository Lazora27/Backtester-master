import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'CenterOfGravity': 1.0
        })
    )
