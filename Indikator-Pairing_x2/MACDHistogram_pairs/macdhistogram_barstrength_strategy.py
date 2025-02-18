import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und BarStrength
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'BarStrength': 1.0
        })
    )
