import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'WeightedCycle': 1.0
        })
    )
