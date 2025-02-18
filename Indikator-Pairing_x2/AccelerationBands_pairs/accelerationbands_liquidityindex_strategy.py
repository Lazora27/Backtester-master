import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'LiquidityIndex': 1.0
        })
    )
