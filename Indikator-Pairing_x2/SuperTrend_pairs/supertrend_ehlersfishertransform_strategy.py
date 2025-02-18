import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
