import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
