import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und VWAPBands
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'VWAPBands': 1.0
        })
    )
