import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'CycleFinder': 1.0
        })
    )
