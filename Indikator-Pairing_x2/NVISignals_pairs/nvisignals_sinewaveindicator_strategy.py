import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
