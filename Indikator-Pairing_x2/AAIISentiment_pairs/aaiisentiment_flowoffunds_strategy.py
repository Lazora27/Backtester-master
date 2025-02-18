import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'FlowOfFunds': 1.0
        })
    )
