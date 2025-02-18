import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BarStrength': 1.0
        })
    )
