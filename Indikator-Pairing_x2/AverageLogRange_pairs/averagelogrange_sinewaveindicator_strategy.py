import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
