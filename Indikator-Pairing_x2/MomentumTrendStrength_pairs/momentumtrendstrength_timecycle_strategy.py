import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'TimeCycle': 1.0
        })
    )
