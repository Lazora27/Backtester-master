import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
