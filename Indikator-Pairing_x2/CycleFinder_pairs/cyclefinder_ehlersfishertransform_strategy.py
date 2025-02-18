import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
