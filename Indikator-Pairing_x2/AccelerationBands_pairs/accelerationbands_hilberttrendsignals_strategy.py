import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
