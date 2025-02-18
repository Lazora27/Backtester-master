import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'CCITurbo': 1.0
        })
    )
