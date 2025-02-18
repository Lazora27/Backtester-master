import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
