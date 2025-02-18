import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und DemandIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'DemandIndex': 1.0
        })
    )
