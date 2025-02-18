import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
