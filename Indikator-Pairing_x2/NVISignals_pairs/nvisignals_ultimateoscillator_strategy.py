import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'UltimateOscillator': 1.0
        })
    )
