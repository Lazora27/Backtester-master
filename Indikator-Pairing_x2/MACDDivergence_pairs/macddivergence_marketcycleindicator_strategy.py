import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
