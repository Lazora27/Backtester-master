import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'FlowOfFunds': 1.0
        })
    )
