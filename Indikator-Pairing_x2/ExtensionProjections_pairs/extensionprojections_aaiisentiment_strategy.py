import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'AAIISentiment': 1.0
        })
    )
