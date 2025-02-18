import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
