import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
