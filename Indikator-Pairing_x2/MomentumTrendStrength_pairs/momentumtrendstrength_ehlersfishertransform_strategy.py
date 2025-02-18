import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
