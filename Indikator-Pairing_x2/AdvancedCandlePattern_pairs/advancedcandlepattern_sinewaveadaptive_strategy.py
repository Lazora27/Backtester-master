import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
