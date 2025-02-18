import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
