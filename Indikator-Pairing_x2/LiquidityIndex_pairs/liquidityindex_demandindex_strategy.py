import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
