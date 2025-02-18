import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'LiquidityIndex': 1.0
        })
    )
