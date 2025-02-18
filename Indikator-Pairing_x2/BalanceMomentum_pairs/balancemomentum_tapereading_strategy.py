import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TapeReading
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TapeReading': 1.0
        })
    )
