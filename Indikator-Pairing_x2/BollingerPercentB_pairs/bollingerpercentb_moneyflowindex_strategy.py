import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
