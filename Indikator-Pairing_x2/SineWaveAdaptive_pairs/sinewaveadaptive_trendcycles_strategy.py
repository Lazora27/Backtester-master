import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'TrendCycles': 1.0
        })
    )
