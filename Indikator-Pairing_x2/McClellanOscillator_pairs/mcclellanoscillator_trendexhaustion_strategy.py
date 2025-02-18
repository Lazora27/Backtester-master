import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'TrendExhaustion': 1.0
        })
    )
