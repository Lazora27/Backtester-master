import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CycleFinder
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CycleFinder': 1.0
        })
    )
