import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'AccelerationBands': 1.0
        })
    )
