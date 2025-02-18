import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
