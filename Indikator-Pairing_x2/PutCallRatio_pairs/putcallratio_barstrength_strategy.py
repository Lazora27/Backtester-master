import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und BarStrength
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'BarStrength': 1.0
        })
    )
