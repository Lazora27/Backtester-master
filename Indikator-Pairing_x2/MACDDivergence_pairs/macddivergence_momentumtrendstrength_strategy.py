import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
