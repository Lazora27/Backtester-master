import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
