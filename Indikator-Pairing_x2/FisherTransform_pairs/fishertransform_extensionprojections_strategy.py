import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ExtensionProjections': 1.0
        })
    )
