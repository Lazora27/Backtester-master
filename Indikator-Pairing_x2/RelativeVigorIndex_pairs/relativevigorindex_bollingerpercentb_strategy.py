import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
