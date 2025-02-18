import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TrendCycles': 1.0
        })
    )
