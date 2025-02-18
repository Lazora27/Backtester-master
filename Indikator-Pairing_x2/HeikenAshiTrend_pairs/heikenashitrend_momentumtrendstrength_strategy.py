import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
