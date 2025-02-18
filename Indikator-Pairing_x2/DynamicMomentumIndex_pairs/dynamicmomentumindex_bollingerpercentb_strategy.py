import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
