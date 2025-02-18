import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
