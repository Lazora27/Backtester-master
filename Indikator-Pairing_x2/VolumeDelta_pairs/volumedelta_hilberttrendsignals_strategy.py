import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
