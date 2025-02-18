import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
