import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
