import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
