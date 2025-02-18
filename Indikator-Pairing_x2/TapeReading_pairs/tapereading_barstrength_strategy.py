import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BarStrength
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BarStrength': 1.0
        })
    )
