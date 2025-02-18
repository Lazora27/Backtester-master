import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und MassIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'MassIndex': 1.0
        })
    )
