import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
