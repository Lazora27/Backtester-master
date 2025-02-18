import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'ModifiedATR': 1.0
        })
    )
