import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'AccelerationBands': 1.0
        })
    )
