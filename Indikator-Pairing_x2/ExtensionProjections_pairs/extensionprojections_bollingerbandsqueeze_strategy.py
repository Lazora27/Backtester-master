import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
