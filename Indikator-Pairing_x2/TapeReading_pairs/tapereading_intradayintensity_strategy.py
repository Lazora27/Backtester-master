import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'IntradayIntensity': 1.0
        })
    )
