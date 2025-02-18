import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
