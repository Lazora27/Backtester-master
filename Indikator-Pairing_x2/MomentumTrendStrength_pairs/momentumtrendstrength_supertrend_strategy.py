import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'SuperTrend': 1.0
        })
    )
