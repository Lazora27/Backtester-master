import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BarStrength
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BarStrength': 1.0
        })
    )
