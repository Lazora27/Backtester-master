import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'CycleFinder': 1.0
        })
    )
