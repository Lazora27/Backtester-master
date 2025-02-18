import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
