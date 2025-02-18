import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SuperTrend
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SuperTrend': 1.0
        })
    )
