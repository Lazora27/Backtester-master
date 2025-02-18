import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'LiquidityIndex': 1.0
        })
    )
