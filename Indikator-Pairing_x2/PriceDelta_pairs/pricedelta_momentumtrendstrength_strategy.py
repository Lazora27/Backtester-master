import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
