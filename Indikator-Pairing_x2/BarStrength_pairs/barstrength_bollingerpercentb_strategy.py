import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'BollingerPercentB': 1.0
        })
    )
