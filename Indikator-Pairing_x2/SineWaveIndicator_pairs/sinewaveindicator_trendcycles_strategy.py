import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SineWaveIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
