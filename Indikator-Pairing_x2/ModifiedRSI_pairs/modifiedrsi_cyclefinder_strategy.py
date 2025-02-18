import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
