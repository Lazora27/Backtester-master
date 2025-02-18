import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
