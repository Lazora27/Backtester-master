import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und GannFans
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'GannFans': 1.0
        })
    )
