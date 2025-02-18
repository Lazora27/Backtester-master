import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'BollingerPercentB': 1.0
        })
    )
