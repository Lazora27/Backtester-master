import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und BarStrength
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'BarStrength': 1.0
        })
    )
