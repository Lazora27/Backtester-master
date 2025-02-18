import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
