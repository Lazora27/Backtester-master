import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
