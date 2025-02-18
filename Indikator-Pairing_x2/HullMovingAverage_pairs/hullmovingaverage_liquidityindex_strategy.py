import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'LiquidityIndex': 1.0
        })
    )
