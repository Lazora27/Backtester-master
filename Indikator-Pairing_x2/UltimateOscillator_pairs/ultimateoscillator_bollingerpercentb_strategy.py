import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
