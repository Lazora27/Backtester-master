import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
