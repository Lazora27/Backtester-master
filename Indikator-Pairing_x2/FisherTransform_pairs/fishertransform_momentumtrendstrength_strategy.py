import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
