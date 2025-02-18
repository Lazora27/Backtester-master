import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
