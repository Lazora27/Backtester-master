import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
