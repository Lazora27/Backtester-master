import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
