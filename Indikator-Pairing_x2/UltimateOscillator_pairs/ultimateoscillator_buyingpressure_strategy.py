import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
