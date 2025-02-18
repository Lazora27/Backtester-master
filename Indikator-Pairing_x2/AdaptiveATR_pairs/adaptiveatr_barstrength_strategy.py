import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und BarStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'BarStrength': 1.0
        })
    )
