import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BollingerPercentB': 1.0
        })
    )
