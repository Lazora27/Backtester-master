import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CycleFinder': 1.0
        })
    )
