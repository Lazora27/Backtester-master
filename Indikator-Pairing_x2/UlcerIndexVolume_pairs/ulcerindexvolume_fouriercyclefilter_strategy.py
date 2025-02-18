import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
