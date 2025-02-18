import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
