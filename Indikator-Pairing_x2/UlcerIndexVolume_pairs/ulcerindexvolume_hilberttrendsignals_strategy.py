import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
