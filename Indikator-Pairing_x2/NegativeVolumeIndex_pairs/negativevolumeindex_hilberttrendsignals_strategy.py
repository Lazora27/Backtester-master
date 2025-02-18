import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
