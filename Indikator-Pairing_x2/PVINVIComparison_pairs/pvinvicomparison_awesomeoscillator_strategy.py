import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
