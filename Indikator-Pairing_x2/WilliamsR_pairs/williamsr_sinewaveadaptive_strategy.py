import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
