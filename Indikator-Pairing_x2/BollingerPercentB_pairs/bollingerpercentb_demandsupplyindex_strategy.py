import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
