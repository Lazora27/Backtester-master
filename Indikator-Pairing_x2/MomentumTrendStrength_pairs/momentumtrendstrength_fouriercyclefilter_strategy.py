import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
