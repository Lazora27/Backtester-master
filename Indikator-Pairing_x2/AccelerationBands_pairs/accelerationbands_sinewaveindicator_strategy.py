import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
