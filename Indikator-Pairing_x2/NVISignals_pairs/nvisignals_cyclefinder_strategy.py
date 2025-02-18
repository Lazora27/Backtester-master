import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CycleFinder
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CycleFinder': 1.0
        })
    )
