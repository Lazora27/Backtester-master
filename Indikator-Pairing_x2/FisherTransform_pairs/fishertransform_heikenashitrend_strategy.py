import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
