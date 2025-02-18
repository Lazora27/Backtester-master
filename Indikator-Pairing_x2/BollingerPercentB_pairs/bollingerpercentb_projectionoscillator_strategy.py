import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
