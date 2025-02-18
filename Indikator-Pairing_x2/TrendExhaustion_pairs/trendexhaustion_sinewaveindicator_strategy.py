import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
