import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'BollingerPercentB': 1.0
        })
    )
