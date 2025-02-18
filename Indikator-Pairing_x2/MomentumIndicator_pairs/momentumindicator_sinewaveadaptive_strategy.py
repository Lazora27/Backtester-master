import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
