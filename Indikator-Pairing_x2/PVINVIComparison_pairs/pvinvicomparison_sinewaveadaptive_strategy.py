import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
