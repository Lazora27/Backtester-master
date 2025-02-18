import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
