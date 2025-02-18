import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
