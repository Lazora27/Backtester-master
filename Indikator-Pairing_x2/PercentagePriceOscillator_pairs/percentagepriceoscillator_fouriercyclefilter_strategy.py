import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
