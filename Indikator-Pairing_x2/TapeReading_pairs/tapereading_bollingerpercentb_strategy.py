import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BollingerPercentB': 1.0
        })
    )
