import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'LiquidityIndex': 1.0
        })
    )
