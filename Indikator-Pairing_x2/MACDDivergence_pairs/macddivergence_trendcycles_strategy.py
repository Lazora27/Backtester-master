import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TrendCycles': 1.0
        })
    )
