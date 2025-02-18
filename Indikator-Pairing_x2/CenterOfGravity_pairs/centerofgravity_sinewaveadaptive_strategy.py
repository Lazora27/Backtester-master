import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
