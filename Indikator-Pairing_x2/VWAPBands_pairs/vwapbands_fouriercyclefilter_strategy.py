import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
