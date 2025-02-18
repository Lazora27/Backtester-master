import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BarStrength': 1.0
        })
    )
