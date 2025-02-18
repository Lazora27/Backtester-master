import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
