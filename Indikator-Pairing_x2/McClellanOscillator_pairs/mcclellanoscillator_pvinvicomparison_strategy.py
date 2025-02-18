import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PVINVIComparison': 1.0
        })
    )
