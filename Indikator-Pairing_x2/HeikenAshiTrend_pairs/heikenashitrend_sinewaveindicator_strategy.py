import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
