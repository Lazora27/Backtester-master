import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'BollingerBands': 1.0
        })
    )
