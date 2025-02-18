import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
