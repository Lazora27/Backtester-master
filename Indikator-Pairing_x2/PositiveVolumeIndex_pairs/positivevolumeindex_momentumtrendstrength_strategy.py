import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
