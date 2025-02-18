import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
