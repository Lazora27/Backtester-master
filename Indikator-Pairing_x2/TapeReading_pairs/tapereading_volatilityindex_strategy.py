import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'VolatilityIndex': 1.0
        })
    )
