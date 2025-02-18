import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'EhlersDecycler': 1.0
        })
    )
