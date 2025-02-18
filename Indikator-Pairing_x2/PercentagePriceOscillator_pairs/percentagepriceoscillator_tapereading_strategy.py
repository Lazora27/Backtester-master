import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
