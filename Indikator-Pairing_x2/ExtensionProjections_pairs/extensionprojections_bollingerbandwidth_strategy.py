import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
