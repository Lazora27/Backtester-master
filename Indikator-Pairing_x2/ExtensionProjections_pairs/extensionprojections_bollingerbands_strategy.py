import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BollingerBands': 1.0
        })
    )
