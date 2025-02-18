import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'CycleFinder': 1.0
        })
    )
