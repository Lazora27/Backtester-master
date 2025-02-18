import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
