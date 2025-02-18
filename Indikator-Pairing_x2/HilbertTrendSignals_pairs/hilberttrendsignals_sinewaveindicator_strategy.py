import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
