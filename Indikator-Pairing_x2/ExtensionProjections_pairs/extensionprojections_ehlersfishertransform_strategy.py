import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
