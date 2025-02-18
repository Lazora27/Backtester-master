import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
