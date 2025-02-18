import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'PhaseDivergence': 1.0
        })
    )
