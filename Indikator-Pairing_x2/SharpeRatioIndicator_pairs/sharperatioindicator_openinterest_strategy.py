import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
