import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'ProjectionBands': 1.0
        })
    )
