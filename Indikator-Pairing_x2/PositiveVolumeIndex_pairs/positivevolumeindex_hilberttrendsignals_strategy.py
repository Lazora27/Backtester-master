import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
