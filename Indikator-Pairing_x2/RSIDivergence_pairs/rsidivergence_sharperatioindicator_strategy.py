import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
