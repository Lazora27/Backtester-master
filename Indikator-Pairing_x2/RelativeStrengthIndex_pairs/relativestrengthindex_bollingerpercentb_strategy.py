import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
