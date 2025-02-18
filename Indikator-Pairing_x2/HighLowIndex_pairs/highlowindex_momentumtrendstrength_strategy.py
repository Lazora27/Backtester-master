import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
