import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
