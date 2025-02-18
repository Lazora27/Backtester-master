import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'FlowOfFunds': 1.0
        })
    )
