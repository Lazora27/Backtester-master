import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
