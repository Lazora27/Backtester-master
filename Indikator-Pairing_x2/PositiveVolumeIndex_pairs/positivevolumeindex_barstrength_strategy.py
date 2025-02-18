import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'BarStrength': 1.0
        })
    )
