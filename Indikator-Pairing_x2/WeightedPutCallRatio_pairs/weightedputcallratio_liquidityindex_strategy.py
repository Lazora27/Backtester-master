import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'LiquidityIndex': 1.0
        })
    )
