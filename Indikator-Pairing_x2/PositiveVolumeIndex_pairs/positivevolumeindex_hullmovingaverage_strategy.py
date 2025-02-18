import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'HullMovingAverage': 1.0
        })
    )
