import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
