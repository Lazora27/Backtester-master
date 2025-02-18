import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BarStrength': 1.0
        })
    )
