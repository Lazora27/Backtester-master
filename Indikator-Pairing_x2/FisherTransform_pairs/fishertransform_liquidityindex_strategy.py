import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'LiquidityIndex': 1.0
        })
    )
