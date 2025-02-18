import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'CycleFinder': 1.0
        })
    )
