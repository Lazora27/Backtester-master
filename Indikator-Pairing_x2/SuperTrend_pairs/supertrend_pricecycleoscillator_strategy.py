import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
