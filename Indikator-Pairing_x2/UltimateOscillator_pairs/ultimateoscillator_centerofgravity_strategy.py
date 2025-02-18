import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
