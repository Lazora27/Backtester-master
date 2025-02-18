import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
