import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'AAIISentiment': 1.0
        })
    )
