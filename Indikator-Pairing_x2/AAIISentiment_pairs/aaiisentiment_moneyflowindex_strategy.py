import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
