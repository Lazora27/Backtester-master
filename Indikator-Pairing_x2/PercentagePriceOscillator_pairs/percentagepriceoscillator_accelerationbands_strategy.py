import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'AccelerationBands': 1.0
        })
    )
