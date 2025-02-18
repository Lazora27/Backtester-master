import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffWaveIndicator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffWaveIndicator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WyckoffWaveIndicator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
