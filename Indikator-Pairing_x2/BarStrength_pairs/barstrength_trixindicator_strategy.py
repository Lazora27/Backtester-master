import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TRIXIndicator': 1.0
        })
    )
