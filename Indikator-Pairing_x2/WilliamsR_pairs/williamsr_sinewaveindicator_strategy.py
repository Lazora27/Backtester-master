import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
