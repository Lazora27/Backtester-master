import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BollingerPercentB': 1.0
        })
    )
