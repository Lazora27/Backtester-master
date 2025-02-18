import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
