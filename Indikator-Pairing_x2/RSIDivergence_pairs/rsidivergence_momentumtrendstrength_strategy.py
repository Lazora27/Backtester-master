import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
