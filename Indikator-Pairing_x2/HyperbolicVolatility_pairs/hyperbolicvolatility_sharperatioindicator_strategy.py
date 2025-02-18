import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
