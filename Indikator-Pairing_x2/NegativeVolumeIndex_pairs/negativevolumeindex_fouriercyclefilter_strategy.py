import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
