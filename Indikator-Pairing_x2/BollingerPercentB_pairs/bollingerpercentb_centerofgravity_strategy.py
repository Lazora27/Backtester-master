import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'CenterOfGravity': 1.0
        })
    )
