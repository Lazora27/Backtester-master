import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
