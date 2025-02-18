import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'LiquidityIndex': 1.0
        })
    )
