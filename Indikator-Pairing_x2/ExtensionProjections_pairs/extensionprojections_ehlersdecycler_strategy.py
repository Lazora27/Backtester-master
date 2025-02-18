import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'EhlersDecycler': 1.0
        })
    )
